from django.contrib.auth import get_user_model

from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'name', 'postal_code',
                  'address', 'neighborhood', 'city', 'state')
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 5},
            'address': {'read_only': True},
            'neighborhood': {'read_only': True},
            'city': {'read_only': True},
            'state': {'read_only': True},
        }

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)
