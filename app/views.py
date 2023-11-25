from django.shortcuts import render
from app.models import *
from app.serializers import *
from app.serializers import employeemodelserializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def employeedata(request):
    EMPDATA=employee.objects.all()
    EMPJSONDATA=employeemodelserializer(EMPDATA,many=True)
    return Response (EMPJSONDATA.data)