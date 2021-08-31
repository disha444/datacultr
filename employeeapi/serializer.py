from rest_framework import serializers
from .models import Employee, Empdetails

class Empserializer(serializers.Serializer):
    class Meta:
        model = Employee
        fields = '__all__'

class Emplserializer(serializers.Serializer):
    class Meta:
        model = Empdetails
        fields = '__all__'
