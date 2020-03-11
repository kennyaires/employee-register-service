from rest_framework import generics

from employee.serializers import EmployeeSerializer


class CreateEmployeeView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = EmployeeSerializer
