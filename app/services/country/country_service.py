from ...protos import CountryServicer, CountryMultipleResponse, add_CountryServicer_to_server
from ...utils import parser_all_object
from ...models import Countries
from ..bootstrap import grpc_server

class CountryService(CountryServicer):
	def get_all(self, request, context):
		print('request')
		countries = parser_all_object(Countries.objects.all())
		response = CountryMultipleResponse(country=countries)

		return response

def start_country_service():
	print('get up')
	add_CountryServicer_to_server(CountryService(), grpc_server)