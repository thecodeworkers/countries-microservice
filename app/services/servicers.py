from .country import start_country_service
from .state import start_state_service

def start_all_servicers():
    start_country_service()
    start_state_service()
    pass

def start_all_emiters():
    pass
