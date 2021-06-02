from django.shortcuts import render
from django.views import view
from django.http import HttpResponse
from django.shortcuts import render

from .models import *

from django.utils import timezone
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

import pprint
class IndexView(View):
    allPosts = Post.objects.order_by("-pubDate")
    def get(self, request):
        form = AuthenticationForm()

        context = {
            'form': form,
            'allPosts': self.allPosts,
            'user': request.user,
        }
        return render(requet, 'posts/index.html', context)
    def post(self, request):
        if 'logout' in request.POST.keys():
            logout(request)

            form = AuthenticationForm()
        else:
            form = AuthenticationForm(data=request.POST)

            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                user = authenticate(username = username, password = password)
                if user is not None:
                    login(request, user = user)

                context = {
                    'form': form,
                    'allPosts': self.allPosts,
                }

                return render(request, 'posts/index.html', context)
class UsernameView(View):
    context = {}

    def get(self, request, username):
        thisUser = User.objects.get(username = username)
        thisUsersPosts = Post.objects.filter(
        userPosted = thisUser).order_by('-pubDate')
        self.context['thisUser'] = thisUser
        self.context['thisUsersPosts'] = thisUsersPosts
        if request.user.username == username:
            form = PostForm()
            self.context['me'] = request.user
            self.context['form'] = form
            return render(request, 'posts/usernamepage.html', self.context)
        else:
            if request.user.is_authenticated:
                self.context['me'] = request.user
                return render(request, 'posts/usernamepage.html', self.context)
            else:
                return render(request, 'posts/usernamepage.html', self.context)
    def post(self, request, username):
        if request.user.is_authenticated:
            newPost = Post(
                userPosted = request.user,
                postText = request.POST['postText'],
                pubDate = timezone.now(),
            )
            newPost.save()
            return self.get(request, username)
class FollowedView(View):
    def get_followed(self, username):
        follower = User.objects.get(username = username)
        entries = Following.objects.filter(follower = follower)
        followed = []
        for entry in entries:
            followed.append(entry.followed)
        return followed

    def get(self, request, username):
        if request.user.is_authenticated:
            if request.user.username == username:
                followed = self.get_followed(username)
                followedPosts = []
                for user in followed:
                    followedPosts += Post.objects.filter(userPosted = user)
                followedPosts = sorted(
                    followedPosts,
                    key = lambda post: post.pubDate,
                    reverse = True
                )
                print(followedPosts)
                return HttpResponse('Blah')
            else:
                return HttpResponse(
                    'You do not have permission to view this page'
                )
        else:
            return HttpResponse(
                'You do not have permission to view this page'
            )
    def post(self, request, username):
        if request.user.is_authenticated:
            pass
        else:
            return HttpResponse(
                'You do not have permission to view this page'
            )
