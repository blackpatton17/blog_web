from django.shortcuts import render
from blog.models import Article
import markdown
# Create your views here.
def index(request):
    blog = Article.objects.get(id = 1)
    blog_title = blog.title
    blog_content = blog.content
    return render(request, 'blog.html', {'blog': blog_title, 'blog_content': blog_content})

def intro(request):
    blog = Article.objects.get(title = "intro")
    blog_title = blog.title
    blog_content = blog.content
    return render(request, 'blog.html', {'blog': blog_title, 'blog_content': blog_content})
