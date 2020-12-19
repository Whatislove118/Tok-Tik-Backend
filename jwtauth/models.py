from datetime import date

from django.db import models

# Create your models here.
from accounts.models import User


class RefreshToken(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    last_login_in = models.DateTimeField(default=date.today(), null=False)
    refresh_token = models.CharField(max_length=255, null=False)

    class Meta:
        managed = False
        db_table = 'jwt_refresh_token'

