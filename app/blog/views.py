from django.shortcuts import render, redirect
from .models import Post, Comment, Category
from django.contrib.auth.decorators import login_required

def home(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, "index.html", context)

@login_required(login_url="login")
def createpost(request):
    if request.method == "GET":
        return render(request, 'createpost.html')
    elif request.method == "POST":
        title = request.POST.get('title')
        subtitle = request.POST.get('subtitle')
        slug = request.POST.get('slug')
        author = request.user
        content = request.POST.get('content')
        image = request.FILES.get("image")

        Post.objects.create(
            title = title,
            subtitle = subtitle,
            slug = slug,
            author = author,
            content = content,
            image = image
        )

        return redirect(home)
    else:
        return render(request, 'createpost.html')
    

def post(request, id):
    post = Post.objects.filter(id=id)
    context = {
        'post':post
    }
    return render(request, "post.html", context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')