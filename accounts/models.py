from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    verified = models.BooleanField(default=False)
    # If you want to allow a Text or CharField to be empty, use this pairing
    #   of default="" and blank=True instead of null=True.
    #   c.f.: https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.Field.null
    bio = models.TextField(default="", blank=True)
    location = models.CharField(max_length=100, default="", blank=True)

class Post(models.Model):
    account = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )
    comment = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null= True
    )

    title = models.CharField(max_length=50, null=True)
    text= models.CharField(max_length=100, null=True)

    pubDate = models.DateTimeField(auto_now_add=True, null=True)

    likes = models.IntegerField(default=0)
    shares = models.IntegerField(null=True)

    def __str__(self):
        return self.title

class Following(models.Model):
    """
    This model will allow us to track followers for each user.
    """
    follower = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        null = True,
        related_name = 'follower',
    )
    followed = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        null = True,
        related_name = 'followed',
    )

    def __str__(self):
        followStr = self.follower.username + " is following "
        followStr += self.followed.username
        return followStr
