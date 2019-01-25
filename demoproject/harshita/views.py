from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to Student Application.")

def addstudent(request):
    return HttpResponse("Student Registration.")


