from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('<username>/followed', views.FollowedView.as_view(), name="followed"),
    path('<username>', views.UsernameView.as_view(), name="username"),
]
