import requests

from app.settings import ADDRESS_SERVICE_URL, ADDRESS_SERVICE_AUTH_TOKEN


def get_full_address(postal_code):
    """Call microservice to get address details from postal code"""
    response = requests.get(
        url=f'{ADDRESS_SERVICE_URL}/{postal_code}',
        headers={'Authorization': f'Bearer {ADDRESS_SERVICE_AUTH_TOKEN}'},
    )
    if response:
        return response.json()
    return dict()
