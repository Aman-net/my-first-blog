from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect


def home(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/postblog.html', {'posts': posts})

def about(request):
    return render(request, 'pages/about.html', {}) 

def contact(request):
    return render(request, 'pages/contact.html', {}) 

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect ('/home.html')
    else:
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})


    