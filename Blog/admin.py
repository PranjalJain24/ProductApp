from django.contrib import admin

# Register your models here.
from Blog.models import Article
admin.site.register(Article)