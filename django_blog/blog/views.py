from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# def test(request):
#     return render(request, 'blog/base.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("upassword")
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/home')
        else:
            return render(request, 'blog/login.html', {'error': 'Invalid credentials'})
    return render(request, 'blog/login.html')


def signup(request):
    if request.method == "POST":
        name = request.POST.get("uname")
        email = request.POST.get("uemail")
        password = request.POST.get("upassword")
        newUser = User.objects.create_user(username=name, email=email, password=password)
        newUser.save()
        return redirect('/login')
    
    return render(request, 'blog/signup.html')

@login_required(login_url='/login')
def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)



@login_required(login_url='/login')
def newPost(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        post = models.Post(title=title, content=content, author=request.user)
        post.save()
        return redirect('/home')
    return render(request, 'blog/newpost.html')


@login_required(login_url='/login')
def myPosts(request):
    context = {
        'posts' : Post.objects.filter(author=request.user)
    }
    return render(request, 'blog/mypost.html', context)



@login_required(login_url='/login')
def signOut(request):
    logout(request)
    return redirect('/login')