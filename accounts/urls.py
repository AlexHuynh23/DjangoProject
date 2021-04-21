from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('profile/', views.profile),
    path('featured/', views.featured),
    path('friends/', views.friends),
    path('likes/', views.likes),
]
