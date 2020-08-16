from ...protos import CountryServicer, CountryMultipleResponse, add_CountryServicer_to_server
from ...utils import parser_all_object
from ...models import Countries, States, Cities
from ..bootstrap import grpc_server

class CountryService(CountryServicer):
	def get_all(self, request, context):

		countries = Countries.objects.all()
		countries = parser_all_object(countries)
		
		countries = map(self.__iterate, countries)
		countries = list(countries)

		return countries

	def __iterate(self, object):
		states = self.__nextLevel(States, object, 'states')
        
		object['states'] = states

		return object

	def __nextLevel(self, model, instance, key):
		states = list()
		for i in instance[key]:
			coincidence = model.objects.get(id=i['$oid'])

			cities = list()

			for j in coincidence.cities:
				cities.append({'name': j.name})

			states.append({'name': coincidence.name, 'cities': cities})

		return states

def start_country_service():
	add_CountryServicer_to_server(CountryService(), grpc_server)