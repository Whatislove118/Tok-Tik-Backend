from django.urls import path

from video.views import add_video, get_video, get_all_videos, like_video, get_audio, add_comments, get_comments, \
    like_comments, get_video_with_hashtags

urlpatterns = [
    path('add/', add_video),
    path('', get_video),
    path('all/', get_all_videos),
    path('like/', like_video),
    path('audio/', get_audio),
    path('add_comments/', add_comments),
    path('get_comments/', get_comments),
    path('like_comments/', like_comments),
    path('hashtags/', get_video_with_hashtags)
]