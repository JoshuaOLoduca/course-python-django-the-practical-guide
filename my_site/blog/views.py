from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(req):
    return HttpResponse("main")


def posts(req):
    return HttpResponse("posts")


def post(req, post):
    print(post)
    return HttpResponse("Post for " + post)
