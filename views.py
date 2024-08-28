# views.py
from django.shortcuts import render, get_object_or_404
from .models import Blog, Video, Picture

def blog_detail(request, username, blog_id):
    blog = get_object_or_404(Blog, id=blog_id, username=username)
    return render(request, 'blog_detail.html', {'blog': blog})

def video_detail(request, username, video_id):
    video = get_object_or_404(Video, id=video_id, username=username)
    return render(request, 'video_detail.html', {'video': video})

def picture_detail(request, username, picture_id):
    picture = get_object_or_404(Picture, id=picture_id, username=username)
    return render(request, 'picture_detail.html', {'picture': picture})
