from datetime import date

from django.db import models

# Create your models here.
from accounts.models import User
from video.models import Video


class UserStatistics(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='user_statistics_id',
                              related_query_name='user_statistics_id', db_column='id')
    amount_videos = models.IntegerField(null=False, default=0)
    likes_on_videos = models.IntegerField(null=False, default=0)
    count_followers = models.IntegerField(null=False, default=0)

    class Meta:
        managed = False
        db_table = 'user_statistics'

class Followers(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_id',
                              related_query_name='user_id', db_column='user_id')
    follower_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='follower_id',
                              related_query_name='follower_id', db_column='follower_id')

    class Meta:
        managed = False
        db_table = 'followers'


class VideoStatistics(models.Model):
    id = models.OneToOneField(Video, primary_key=True, on_delete=models.CASCADE, related_name='video_statistics_id',
                              related_query_name='video_statistics_id', db_column='video_id')
    likes = models.IntegerField(null=False, default=0, db_column='likes')
    share_video = models.CharField(max_length=300, db_column='share_video')

    class Meta:
        managed = False
        db_table = 'video_statistics'

class VideoComments(models.Model):
    id = models.AutoField(primary_key=True)
    video_id = models.OneToOneField(Video, on_delete=models.CASCADE, related_name='video_comments_id',
                              related_query_name='video_comments_id', db_column='video_id')
    username = models.CharField(max_length=100)
    comment = models.CharField(max_length=300)
    likes = models.IntegerField(default=0)
    date_of_published = models.DateField(auto_created=date.today(), default=date.today())

    class Meta:
        managed = False
        db_table = 'video_comments'

class Hashtags(models.Model):
    hashtag = models.CharField(max_length=30, primary_key=True)
    count_usages = models.IntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'hashtags'

class HashtagsOnVideo(models.Model):
    id = models.AutoField(primary_key=True)
    video_id = models.OneToOneField(VideoStatistics, on_delete=models.CASCADE, related_name='hastags_video_id', db_column='video_id')
    hashtag = models.OneToOneField(Hashtags, on_delete=models.CASCADE, related_name='hastags_on_statistics', db_column='hashtag')

    class Meta:
        managed = False
        db_table = 'hashtags_on_video'
