from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class Profile(AbstractBaseUser):
    first_name =  models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.username

class Post(models.Model):
    POST_TYPE = (
        ('I', 'Image'),
        ('T', 'Text'),
        ('L', 'Link')
    )

    account = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    type = models.CharField(max_length=1,null=True, choices=POST_TYPE )
    title = models.CharField(max_length=50, null=True)
    text= models.CharField(max_length=100, null=True)

    date_created = models.DateTimeField(auto_now_add=True, null=True)

    likes = models.IntegerField(null=True)
    shares = models.IntegerField(null=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)

    likes = models.IntegerField(null=True)
    shares = models.IntegerField(null=True)
