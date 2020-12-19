from datetime import date

from django.db import models
from accounts.models import User


class ProfileSettings(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='profile_settings_id',
                              related_query_name='profile_settings_id', db_column='id')
    username = models.CharField(max_length=30, null=False, unique=True, default='@id%d')
    date_of_registration = models.DateField(auto_created=date.today(), null=False)
    push_notifications = models.BooleanField(null=False, default=True)
    profile_link = models.CharField(max_length=200, default='id')

    def __str__(self):
        return self.username

    class Meta:
        managed = False
        db_table = 'profile_settings'

class Confidentiality(models.Model):
    id = models.OneToOneField(ProfileSettings, on_delete=models.CASCADE, primary_key=True,
                              related_name='confidentiality_id', related_query_name='confidentiality_id', db_column='id')
    private_account = models.BooleanField(null=False, default=False)
    allow_download_video = models.BooleanField(null=False, default=True)
    comments_filter = models.BooleanField(null=False,default=True)
    allow_private_message = models.TextChoices('allow_private_message', 'all friends nobody')
    allow_likes_list_looking = models.TextChoices('allow_likes_list_looking', 'all me')

    class Meta:
        managed = False
        db_table = 'confidentiality'

class Avatar(models.Model):
    id = models.OneToOneField(ProfileSettings, on_delete=models.CASCADE, primary_key=True,
                              related_name='avatar_id', related_query_name='avatar_id', db_column='id')
    avatar_uri = models.CharField(max_length=200, null=False)
    url = models.URLField(null=False)
    name = models.CharField(max_length=200, null=False)

    class Meta:
        managed = False
        db_table = 'avatar'

class Security(models.Model):
    id = models.OneToOneField(ProfileSettings, on_delete=models.CASCADE, primary_key=True,
                              related_name='security_id', related_query_name='security_id', db_column='id')
    two_step_verification = models.BooleanField(null=False, default=False)
    your_devices = models.TextField(max_length=200, null=False)

    class Meta:
        managed = False
        db_table = 'security'

