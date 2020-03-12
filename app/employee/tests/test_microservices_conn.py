from django.test import TestCase
from microservices import get_full_address


class MicroservicesTests(TestCase):
    """Tets the microservices API communication"""

    def test_get_full_address_connection(self):
        """Test if microservice return full addres details from postal code"""
        valid_postal_code = '09780250'
        result = get_full_address(valid_postal_code)
        self.assertEqual((len(result) > 0), True)

    def test_get_full_address_return_empty_dict(self):
        """Test if microservice returns empty dict from ivalid postal code"""
        invalid_postal_code = 'iNvAlIdo'
        result = get_full_address(invalid_postal_code)
        self.assertEqual((len(result) == 0), True)
