from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog, Category
# Create your views here.

categories = Category.objects.all()


def home(request):
    blogs = Blog.objects.all()

    return render(request, 'blog/home.html', {'blogs': blogs, 'categories': categories})


def detail(request, blog_id):
    b = Blog.objects.get(id=blog_id)

    return render(request, 'blog/detail.html', {'blog': b, 'categories': categories})


def category(request, blog_category):
    c = get_object_or_404(Category, title=blog_category)
    b = Blog.objects.filter(category=c)
    return render(request, 'blog/category.html', {'categories': categories, 'blogs': b})
