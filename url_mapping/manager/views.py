from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
  return HttpResponse("Welcome to manager home page Rabi")

def login(request):
  return HttpResponse("Welcome to manager login page Rabi")