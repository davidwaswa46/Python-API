from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from.models import employees #Name of the model
from.serializers import employeesSerializer #Name of the serializer

class employeeList(APIView):#APIView is used so that the normal views can return API data, This class inherits from APIview

    def get(self,request): #This method is used to return all the employees in the Model
        employees1=employees.objects.all()
        serializer=employeesSerializer(employees1, many=True) #Takes all your objects and converts them into Json 
        return Response(serializer.data)
    

    def post(self): #submits all your data
        pass


