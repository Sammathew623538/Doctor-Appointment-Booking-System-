from dataclasses import fields
from pyexpat import model
from django.forms import ModelChoiceField
from rest_framework import serializers
from.models import Employee, Piller
class Employeeserializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'






class Pillerserializer(serializers.ModelSerializer):
    class Meta:
        model=Piller
        fields='__all__'