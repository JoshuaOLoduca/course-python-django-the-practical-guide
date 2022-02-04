from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(req):
  return HttpResponse("Jan")

def index2(req):
  return HttpResponse("Feb")