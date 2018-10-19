from django.shortcuts import render

from blog.models import Post


def home(request):
    published_posts = Post.objects.filter(is_published=True)
    return render(request, 'blog/home.html', {'posts': published_posts})


def about(request):
    return render(request, 'blog/about.html')
