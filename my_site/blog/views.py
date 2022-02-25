from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(req):
    return render(req, "blog/index.html")
    # return HttpResponse("main")


def posts(req):
    return render(req, "blog/all-posts.html")


def post(req, post):
    print(post)
    return render(req, "blog/post-detail.html")
