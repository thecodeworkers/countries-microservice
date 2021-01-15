from google.protobuf.json_format import MessageToDict
from mongoengine.queryset import NotUniqueError
from ...protos import state_pb2, state_pb2_grpc
from ...utils import parser_all_object, parser_one_object, not_exist_code, exist_code, paginate, parser_context, pagination, default_paginate_schema
from ...utils.validate_session import is_auth
from ..bootstrap import grpc_server
from bson.objectid import ObjectId
from ...models import States, Countries, Cities


class StateService(state_pb2_grpc.StateServicer):
    def table(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '03_state_table')

            search = request.search

            pipeline = [
                {
                    "$lookup": {
                        "from": "cities",
                        "localField": "cities",
                        "foreignField": "_id",
					    "as": "cities"
                    }
                },
                { "$unwind": "$cities" },
                {
                    "$group": {
                        "_id": "$_id",
                        "id": { "$first": { "$toString": "$_id" } },
                        "country": { "$first": { "$toString": "$country" } },
                        "name": { "$first": "$name" },
                        "cities": {
                            "$push": {
                                "id": { "$toString": "$cities._id" },
                                "state": { "$toString": "$cities.state" },
                                "name": "$cities.name",
                            }
                        },
                    }
                },
                {
                    "$project": {
                        "_id": 0,
                    }
                },
                {
                    "$match": {
                        "$or": [
                            { "name": { "$regex": search, "$options": "i" } },
                            { "cities.name": { "$regex": search, "$options": "i" } }
                        ]
                    }
                },
            ]

            pipeline = pipeline + pagination(request.page, request.per_page, { "name": 1 })

            states = States.objects().aggregate(pipeline)

            response = state_pb2.StateTableResponse(**default_paginate_schema(states, request.page, request.per_page))

            return response

        except Exception as error:
            raise Exception(error)

    def get_all(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '03_state_get_all')

            states = parser_all_object(States.objects.all())
            response = state_pb2.StateMultipleResponse(state=states)
        except Exception as error:
            raise Exception(error)

        return response

    def get(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '03_state_get')

            state = States.objects.get(id=request.id)
            state = parser_one_object(state)
            response = state_pb2.StateResponse(state=state)

            return response

        except States.DoesNotExist as e:
            not_exist_code(context, e)

    def save(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '03_state_save')

            state_object = MessageToDict(request)
            country = Countries.objects.get(id=state_object['country'])

            del state_object['country']

            state = States(**state_object)
            state.country = country
            state.save()

            country.update(push__states=state)

            state = parser_one_object(state)

            response = state_pb2.StateResponse(state=state)

            return response

        except NotUniqueError as e:
            exist_code(context, e)

    def update(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '03_state_update')

            state_object = MessageToDict(request)
            state = States.objects.get(id=state_object['id'])

            country = Countries.objects.get(id=state_object['country'])
            state_object['country'] = country

            old_country = Countries.objects.get(id=state.country.id)

            if state:
                del state_object['id']

            state.update(**state_object)

            state = States.objects.get(id=state.id)

            old_country.update(pull__states=state)
            country.update(push__states=state)

            state = parser_one_object(state)
            response = state_pb2.StateResponse(state=state)

            return response

        except NotUniqueError as e:
            exist_code(context, e)

    def delete(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '03_state_delete')

            state = States.objects.get(id=request.id)

            country = Countries.objects.get(id=state.country.id)
            country.update(pull__states=state)

            state = state.delete()
            response = state_pb2.StateEmpty()

            return response

        except States.DoesNotExist as e:
            not_exist_code(context, e)


def start_state_service():
    state_pb2_grpc.add_StateServicer_to_server(StateService(), grpc_server)
