from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def display(request):
    s1='<h1>Hello World</h1>'
    s2='<h2>Welcome IT Vednat</h2>'
    return HttpResponse(s1+s2)
