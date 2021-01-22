from google.protobuf.json_format import MessageToDict
from mongoengine.queryset import NotUniqueError
from ...protos import CountryServicer, CountryMultipleResponse, add_CountryServicer_to_server, country_pb2, country_pb2_grpc
from ...utils import parser_all_object, paginate, parser_one_object, not_exist_code, exist_code, parser_context, pagination, default_paginate_schema
from ...utils.validate_session import is_auth
from ...models import Countries, States, Cities
from bson.objectid import ObjectId
from ..bootstrap import grpc_server
import re

class CountryService(CountryServicer):
    def table(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '03_country_table')

            search = request.search

            pipeline = [
                {
                    "$lookup": {
                        "from": "states",
                        "localField": "states",
                        "foreignField": "_id",
					    "as": "states"
                    }
                },
                { "$unwind": "$states" },
                {
                    "$lookup": {
                        "from": "cities",
                        "localField": "states.cities",
                        "foreignField": "_id",
					    "as": "states.cities"
                    }
                },
                {
                    "$addFields": {
                        "ref_id": "$_id",
                        "states.cities": {
                            "$map": {
                                "input": "$states.cities",
                                "as": "cities",
                                "in": {
                                    "id": { "$toString": "$$cities._id" },
                                    "name": "$$cities.name",
                                    "state": { "$toString": "$$cities.state" }
                                }
                            }
                        }
                    }
                },
                {
                    "$group": {
                        "_id": "$_id",
                        "id": { "$first": { "$toString": "$_id" } },
                        "name": { "$first": "$name" },
                        "code": { "$first": "$code"},
                        "phone_prefix": { "$first": "$phone_prefix" },
                        "active": { "$first": "$active" },
                        "states": {
                            "$push": {
                                "id": { "$toString": "$states._id" },
                                "country": { "$toString": "$states.country" },
                                "name": "$states.name",
                                "cities": "$states.cities"
                            }
                        },
                    }
                },
                {
                    "$project": {
                        "_id": 0,
                        "ref_id": 0
                    }
                },
                {
                    "$match": {
                        "$or": [
                            { "name": { "$regex": search, "$options": "i" } },
                            { "states.name": { "$regex": search, "$options": "i" } },
                            { "states.cities.name": { "$regex": search, "$options": "i" } }
                        ]
                    }
                },
            ]

            pipeline = pipeline + pagination(request.page, request.per_page, { "name": 1 })

            countries = Countries.objects().aggregate(pipeline)

            response = country_pb2.CountryTableResponse(**default_paginate_schema(countries, request.page, request.per_page))

            return response

        except Exception as error:
            raise Exception(error)

    def get_all(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '03_country_get_all')

            countries = parser_all_object(Countries.objects)
            response = country_pb2.CountryMultipleResponse(country=countries)

            return response

        except Exception as error:
            raise Exception(error)

    def get(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '03_country_get')

            country = Countries.objects.get(id=request.id)
            country = parser_one_object(country)

            response = country_pb2.CountryResponse(country=country)

            return response
        except Exception as error:
            raise Exception(error)

    def save(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '03_country_save')

            country_object = MessageToDict(request)
            country_object['phone_prefix'] = country_object['phonePrefix']
            del country_object['phonePrefix']

            country = Countries(**country_object)
            country.save()

            country = parser_one_object(country)
            response = country_pb2.CountryResponse(country=country)

            return response

        except NotUniqueError as error:
            exist_code(context, error)

    def update(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '03_country_update')

            country_object = MessageToDict(request)

            if country_object['phonePrefix']:
                country_object['phonePrefix'] = country_object['phonePrefix']
                del country_object['phonePrefix']

            country = Countries.objects.get(id=country_object['id'])

            country.update(**country_object)

            country = Countries.objects.get(id=country_object['id'])
            country = parser_one_object(country)
            response = country_pb2.CountryResponse(country=country)

            return response
        except NotUniqueError as error:
            exist_code(context, error)

    def delete(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '03_country_delete')

            country = Countries.objects.get(id=request.id)
            country = country.delete()
            response = country_pb2.CountryEmpty()

            return response
        except Countries.DoesNotExist as error:
            not_exist_code(context, error)

def start_country_service():
    add_CountryServicer_to_server(CountryService(), grpc_server)
