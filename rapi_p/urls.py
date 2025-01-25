from django.urls import path
from .views import get_data

app_name='rapi_p'

urlpatterns=[
    path('fetchdata/',get_data,name='get'),
]