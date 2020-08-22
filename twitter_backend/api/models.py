from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class AuthUser(AbstractUser):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_name = models.CharField(max_length=150)
    profile_pic = models.CharField(max_length=500, blank=False, null=False)

    class Meta:
        # managed = False
        db_table = "auth_user"


class Tweet(models.Model):
    id = models.BigAutoField(primary_key=True)
    tweet = models.CharField(max_length=500, null=False, blank=False)
    author = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    flag = models.BooleanField(default=True)

    class Meta:
        db_table = "tweet"


class TweetComment(models.Model):
    id = models.BigAutoField(primary_key=True)
    comment = models.CharField(max_length=500, null=False, blank=False)
    author = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    flag = models.BooleanField(default=True)

    class Meta:
        db_table = "tweet_comment"


class TweetLike(models.Model):
    id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    flag = models.BooleanField(default=True)

    class Meta:
        db_table = "tweet_like"
