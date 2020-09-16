from .country import start_country_service
from .state import start_state_service
from .city import start_city_service

def start_all_servicers():
    start_country_service()
    start_state_service()
    start_city_service()

def start_all_emiters():
    pass
