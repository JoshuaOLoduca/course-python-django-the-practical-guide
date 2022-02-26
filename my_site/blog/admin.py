from django.contrib import admin
from blog.models import *

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_filter = (
        "author",
        "title",
        "tags",
        "date",
    )
    list_display = (
        "title",
        "date",
        "author",
        "get_tags",
    )
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
