from google.protobuf.json_format import MessageToDict
from mongoengine.queryset import NotUniqueError
from ...protos import city_pb2, city_pb2_grpc
from ...utils import parser_all_object, parser_one_object, not_exist_code, exist_code, paginate, parser_context
from ...utils.validate_session import is_auth
from ..bootstrap import grpc_server
from bson.objectid import ObjectId
from ...models import Cities, States


class CityService(city_pb2_grpc.CityServicer):
    def table(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '03_city_table')

            cities = Cities.objects

            search = request.search
            
            if search:
                cities = Cities.objects(__raw__= { '$or': [
                    { 'name' : search}, 
                    {'state': ObjectId(search) if ObjectId.is_valid(search) else search},
                    {'_id': ObjectId(search) if ObjectId.is_valid(search) else search}
                ]})

            response = paginate(cities, request.page, request.per_page)

            response = city_pb2.CityTableResponse(**response)

            return response

        except Exception as error:
            raise Exception(error)

    def get_all(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '03_city_get_all')

            cities = parser_all_object(Cities.objects.all())
            response = city_pb2.CityMultipleResponse(city=cities)

            return response
        except Exception as error:
            raise Exception(error)

    def get(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '03_city_get')

            city = Cities.objects.get(id=request.id)
            city = parser_one_object(city)
            response = city_pb2.CityResponse(city=city)

            return response

        except Cities.DoesNotExist as e:
            not_exist_code(context, e)

    def save(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '03_city_save')

            city_object = MessageToDict(request)

            state = States.objects.get(id=city_object['state'])

            del city_object['state']

            city = Cities(**city_object)
            city.state = state
            city.save()

            state.update(push__cities=city)

            city = parser_one_object(city)

            response = city_pb2.CityResponse(city=city)

            return response

        except NotUniqueError as e:
            exist_code(context, e)

    def update(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '03_city_update')

            city_object = MessageToDict(request)
            city = Cities.objects.get(id=city_object['id'])

            state = States.objects.get(id=city_object['state'])
            city_object['state'] = state

            old_state = States.objects.get(id=city.state.id)

            if city:
                del city_object['id']

            city.update(**city_object)

            city = Cities.objects.get(id=city.id)

            old_state.update(pull__cities=city)
            state.update(push__cities=city)

            city = parser_one_object(city)
            response = city_pb2.CityResponse(city=city)

            return response

        except NotUniqueError as e:
            exist_code(context, e)

    def delete(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '03_city_delete')

            city = Cities.objects.get(id=request.id)

            state = States.objects.get(id=city.state.id)
            state.update(pull__cities=city)

            city = city.delete()
            response = city_pb2.CityEmpty()

            return response

        except Cities.DoesNotExist as e:
            not_exist_code(context, e)


def start_city_service():
    city_pb2_grpc.add_CityServicer_to_server(CityService(), grpc_server)
