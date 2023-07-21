from django.urls import path
from app2.views import *
name='my_app2'

urlpatterns=[
    path('first/',first, name='first'),
    path('second/',second,name='second')
]