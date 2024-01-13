
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def Cyrus(request):
    return HttpResponse("Hello, Cyrus!")

def Radisson(request):
    return HttpResponse("Hello, Radisson")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "esm":name.capitalize()
    })
