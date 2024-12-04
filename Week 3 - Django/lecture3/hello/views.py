from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def sivan(request):
    return HttpResponse("Hello, Sivan!")

def david(request):
    return HttpResponse("Hello, David!")

def brian(request):
    return HttpResponse("Hello, Brian!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")