# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('hoskie/blog/<str:username>/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('hoskie/video/<str:username>/<int:video_id>/', views.video_detail, name='video_detail'),
    path('hoskie/picture/<str:username>/<int:picture_id>/', views.picture_detail, name='picture_detail'),
    path('hoskie/stream/<str:resource_type>/<str:username>/<int:resource_id>/', views.StreamData.as_view(), name='stream_data'),
]
