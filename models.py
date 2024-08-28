# models.py
from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    username = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.TextField()

class Video(models.Model):
    username = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    video_url = models.URLField()

class Image(models.Model):
    username = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

class Feed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, null=True, blank=True, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, null=True, blank=True, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
