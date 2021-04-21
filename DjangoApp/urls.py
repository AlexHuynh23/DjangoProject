"""DjangoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from django.http import HttpResponse

def home(request):
    return HttpResponse('Home page')

def login(request):
    return HttpResponse('Login Page')

def signup(request):
    return HttpResponse('Sign Up Page')

def contact(request):
    return HttpResponse('Contact page')

urlpatterns = [
    path('account/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('', home),
    path('about/', contact),
    path('login/', login),
    path('signup/', signup),
]