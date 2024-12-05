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
    return render(request, "/media/sivan/Data/My (Google) Drive/Extracurriculars (ECs)/(💻) Computer Science/CS50W/Week 3 - Django/lecture3/hello/templates/greet.html", {
        "name": name.capitalize(),
    })