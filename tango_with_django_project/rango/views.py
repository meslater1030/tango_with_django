from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Rango says hey there world! \n"
            "This is the <a href='about/'>about</a> page.")


def about(request):
    return HttpResponse("Rango says here is the about page. \n"
            "This is the <a href='../'>home</a> page.")
