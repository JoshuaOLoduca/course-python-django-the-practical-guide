from operator import index
from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()


class Tag(models.Model):
    caption = models.CharField(max_length=25)


class Post(models.Model):
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="posts"
    )
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=250)
    image_name = models.CharField(max_length=50)
    date = models.DateField()
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField(db_index=True, unique=True)
