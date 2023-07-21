from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first(request):
    return HttpResponse('<h1>first from app1</h1>')

def second(request):
    return HttpResponse('<h1>second from app1</h1>')