#from rest_framework import employees
from .models import employees 
from rest_framework import serializers


class employeesSerializer(serializers.ModelSerializer):

    class Meta:
        model= employees
        #fields=('firstname','lastname')
        fields='__all__'