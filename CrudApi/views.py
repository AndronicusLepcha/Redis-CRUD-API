from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
# Create your views here.

# CREATE
@api_view(['GET'])
def create_data(request):
    
    return HttpResponse("API create_data added the new data in the DB and REDIS !")

# RETRIEVE
@api_view(['GET'])
def retrieve_data(request):
    data=None
    return Response(data)

# UPDATE
@api_view(['GET'])
def update_data(request):
    data=None
    return Response(data)

# DELETE 
@api_view(['GET'])
def delete_data(request):
    data=None
    return Response(data)