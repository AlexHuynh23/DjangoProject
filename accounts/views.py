
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
# Add my models and my forms
from .models import *
from .forms import PostForm
# These are needed for user authentication and persistence
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.utils import timezone

import pprint
class IndexView(View):
    # Makes all posts appear regardless
    allPosts = Post.objects.order_by("-pubDate")

    def get(self, request):
        form = AuthenticationForm()
        # Send the template the form and the posts.
        context = {
            'form': form,
            'allPosts': self.allPosts,
            'user': request.user,
        }
        return render(request, 'accounts/index.html', context)

    def post(self, request):
        # If its the logout button that was pressed
        if 'logout' in request.POST.keys():
            logout(request)
            # Empty form
            form = AuthenticationForm()
        else:
            # If its the login button loads form with data
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                # Then authenticate and log in.
                user = authenticate(username = username, password = password)
                # Checks if the user exists
                if user is not None:
                    login(request, user = user)
        # Set up the data for the template
        context = {
            'form': form,
            'allPosts': self.allPosts,
        }
        # Run template with context
        return render(request, 'accounts/index.html', context)

class UsernameView(View):
    context = {}

    def get(self, request, username):
        # Need to track down the User object before getting Posts
        thisUser = User.objects.get(username = username)
        # I've layered on both a filter and a sort on this query
        thisUsersPosts = Post.objects.filter(
            userPosted = thisUser).order_by('-pubDate')
        self.context['thisUser'] = thisUser
        self.context['thisUsersPosts'] = thisUsersPosts
        if request.user.username == username:
            # If we're here, the user is on their own page.
            form = PostForm()
            self.context['me'] = request.user
            self.context['form'] = form
            return render(request, 'accounts/usernamepage.html', self.context)
        else:
            if request.user.is_authenticated:
                # If we're here, we have an authenticated user but
                # not at their own home page
                self.context['me'] = request.user
                return render(request, 'accounts/usernamepage.html', self.context)
            else:
                # If we're here, we have non-authenticated user
                return render(request, 'accounts/usernamepage.html', self.context)
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
                    key=lambda post: post.pubDate,
                    reverse = True
                )
                print(followedPosts)
                return HttpResponse('Blah')
            else:
                return HttpResponse(
                    'You do not have permission to view this page.'
                )
        else:
            return HttpResponse(
                'You do not have permission to view this page.'
            )

    def post(self, request, username):
        if request.user.is_authenticated:
            pass
        else:
            return HttpResponse(
                'You do not have permission to view this page.'
            )
