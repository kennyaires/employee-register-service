import requests

URL = 'http://viacep.com.br/ws/'


# address_query microservice api call
def get_full_address(postal_code):
    response = requests.get(f'{URL}/{postal_code}/json')
    if response:
        return response.json()
    return dict()
