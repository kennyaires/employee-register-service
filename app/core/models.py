from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
from microservices import get_full_address


class UserManager(BaseUserManager):

    def create_user(self, email, postal_code, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        if not postal_code:
            raise ValueError('Users must have a postal code')

        # Calls microservice api
        postal_code = self.normalize_postal_code(postal_code)
        address_data = get_full_address(postal_code)
        user = self.model(
                        email=self.normalize_email(email),
                        postal_code=postal_code,
                        address=address_data.get('logradouro', ''),
                        neighborhood=address_data.get('bairro', ''),
                        city=address_data.get('localidade', ''),
                        state=address_data.get('uf', ''),
                        **extra_fields
                        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and save a new superuser"""
        user = self.create_user(email, '000', password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

    @classmethod
    def normalize_postal_code(cls, postal_code):
        import re
        return re.sub(r'[^0-9]', '', postal_code)


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    neighborhood = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
