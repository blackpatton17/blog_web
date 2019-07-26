from django.contrib import admin
from blog.models import Blog
from blog.models import Article
# Register your models here.

admin.site.register(Blog)
admin.site.register(Article)
