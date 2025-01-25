from django.shortcuts import render
from django.http.response import JsonResponse
from .dbconnect import api_methods
from .authentication import apikeycheck
from rest_framework.decorators import authentication_classes

@authentication_classes([apikeycheck])
def get_data(request):
    data=api_methods.get_view("Select buscode,busname from ph_business")
    return JsonResponse(data,safe=False)