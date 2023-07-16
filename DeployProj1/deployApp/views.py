from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def display(request):
    s1='<h1>Hello World</h1>'
    s2='<h2>Welcome IT Vedantt</h2>'
    s3='<h3>Good Evening</h3>'
    s4='<h4>Good Bye</h4>'
    return HttpResponse(s1+s2+s3)
