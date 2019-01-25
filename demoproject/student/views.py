from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to New Application.")

def addproject(request):
    return HttpResponse("Project Registration.")
