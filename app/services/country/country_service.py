from ...protos import CountryServicer, CountryMultipleResponse, add_CountryServicer_to_server, country_pb2, country_pb2_grpc
from ...utils import parser_all_object, paginate
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

		countries = parser_all_object(Countries.objects.all())
		print(countries)
		response = country_pb2.CountryMultipleResponse(country=countries)

		return response

def start_country_service():
	add_CountryServicer_to_server(CountryService(), grpc_server)