from django.shortcuts import render, get_object_or_404
from .models import Blog

def my_blog(request):
    blogs= Blog.objects.order_by('-date')
    return render (request, 'blog/my_blog.html', {'blogs': blogs})

def detail(request, blog_id):
    blogs= get_object_or_404(Blog, pk=blog_id)
    return render (request, 'blog/detail.html', {'blog_id': blogs})
