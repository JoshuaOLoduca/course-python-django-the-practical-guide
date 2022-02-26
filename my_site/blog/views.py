from datetime import date
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

# Dummy data
postsDb = []


def get_date(item):
    return item["date"]


def index(req):
    latest = Post.objects.all().order_by("-date")[:3]
    return render(req, "blog/index.html", {"posts": latest})


def posts(req):
    all_posts = Post.objects.all().order_by("-date")
    return render(req, "blog/all-posts.html", {"all_posts": all_posts})


def post(req, slug):
    found_post = get_object_or_404(Post, slug=slug)

    return render(
        req,
        "blog/post-detail.html",
        {"post": found_post, "post_tags": found_post.tags.all()},
    )
