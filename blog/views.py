from django.shortcuts import render
from django.utils import timezone
from .models import Post


def postblog(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/postblog.html', {'posts': posts})

def about(request):
    return render(request, 'pages/about.html', {}) 

def contact(request):
    return render(request, 'pages/contact.html', {}) 



    