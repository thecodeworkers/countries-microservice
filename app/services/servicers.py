from .state import start_state_service
from .city import start_city_service

def start_all_servicers():
    start_state_service()
    start_city_service()
    pass

def start_all_emiters():
    pass
