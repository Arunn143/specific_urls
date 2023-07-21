from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def first(request):
    return HttpResponse('<h2>first from app2')

def second(request):
    return HttpResponse('<h1>second from app2</h1>')