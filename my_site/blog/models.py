from operator import index
from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=25)

    def __str__(self):
        return self.caption


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

    def get_tags(self):
        return ", \n".join([p.caption for p in self.tags.all()])

    def __str__(self):
        return f"{self.title} by {self.author.full_name()}"

    get_tags.short_description = "Tags"
