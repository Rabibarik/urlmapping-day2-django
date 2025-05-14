from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
  return HttpResponse("Welcome to employee home page Rabi")

def login(request):
  return HttpResponse("Welcome to employee login page Rabi")