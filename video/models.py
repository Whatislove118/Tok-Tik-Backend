from django.db import models

# Create your models here.
from accounts.models import User

class Audio(models.Model):
    audio_id = models.AutoField(primary_key=True, db_column='audio_id')
    name = models.CharField(max_length=100, null=False, db_column='name')
    author_name = models.CharField(max_length=100, db_column='author_name')
    amount_videos_with_music = models.IntegerField(db_column='amount_videos_with_music', default=0)
    class Meta:
        managed = False
        db_table = 'audio'



class Video(models.Model):
    video_id = models.AutoField(primary_key=True, db_column='video_id')
    user_id = models.OneToOneField(User, on_delete=models.CASCADE,
                              related_name='video_user_id', related_query_name='video_user_id', db_column='id')
    description = models.CharField(max_length=300, db_column='description')
    audio_id = models.OneToOneField(Audio, on_delete=models.CASCADE, related_name='audio_video_id',
                                    related_query_name='audio_video_id', db_column='audio_id')
    url = models.CharField(max_length=300, null=False, db_column='url')
    uri = models.CharField(max_length=300, db_column='uri')

    class Meta:
        managed = False
        db_table = 'video'


