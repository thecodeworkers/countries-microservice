from google.protobuf.json_format import MessageToDict
from mongoengine.queryset import NotUniqueError
from ...protos import CountryServicer, CountryMultipleResponse, add_CountryServicer_to_server, country_pb2, country_pb2_grpc
from ...utils import parser_all_object, paginate, parser_one_object, not_exist_code
from ...models import Countries, States, Cities
from ..bootstrap import grpc_server

class CountryService(CountryServicer):
	def table(self, request, context):
		try:
			countries = Countries.objects
			response = paginate(states, request.page, request.per_page)

			response = country_pb2.CountryTableResponse(**response)
			
			return response

		except Exception as error:
			raise Exception(error)

	def get_all(self, request, context):
		try:
			countries = parser_all_object(Countries.objects)
			response = country_pb2.CountryMultipleResponse(country=countries)

			return response
		except Exception as error:
			raise Exception(error)

	def get(self, request, context):
		try:
			country = Countries.objects.get(id=request.id)
			country = parser_one_object(country)
			response = country_pb2.CountryResponse(country=country)

			return response
		except Countries.DoesNotExist as error:
			not_exist_code(context, error)
			
	def save(self, request, context):
		try:
			country_object = MessageToDict(request)
			country = Countries(**country_object)
			country.save()
			response = country_pb2.CountryResponse(country=country)

			return response
		except NotUniqueError as error:
			exist_code(context, e)

	def update(self, request, context):
		try:
			country_object = MessageToDict(request)
			country = Countries.objects.get(id=country_object['id'])

			country.update(**country_object)
			response = country_pb2.CountryResponse(country=country)
			return country
		except NotUniqueError as error:
			exist_code(context, error)

	def delete(self, request, context):
		try:
			country = Countries.objects.get(id=request.id)
			country = country.delete()
			response = country_pb2.CountryEmpty()

			return response
		except Countries.DoesNotExist as error:
			not_exist_code(context, e)
		

def start_country_service():
	add_CountryServicer_to_server(CountryService(), grpc_server)