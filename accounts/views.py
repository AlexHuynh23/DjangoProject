from django.shortcuts import render
from django.http import HttpResponse

from .models import *
# Create your views here.

def home(request):
    return HttpResponse("home page")

def featured(request):
    posts = Post.objects.all()
    return render(request, 'accounts/featured.html', {'posts': posts})

def profile(request):
    users = Profile.objects.all()
    posts = Post.objects.all()
    comments = Comment.objects.all()
    return render(request, 'accounts/profile.html', {'users': users, 'posts': posts, 'comments': comments})

def friends(request):
    return HttpResponse("Account friends Page")

def likes(request):
    return HttpResponse("Account Liked Page")
