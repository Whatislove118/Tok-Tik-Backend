from django.db import models
from datetime import date


# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=30, unique=True, null=False)
    password = models.CharField(max_length=30, null=False)
    email = models.EmailField(max_length=30, unique=True, null=False)

    def __str__(self):
        return self.login

    class Meta:
        managed = False
        db_table = 'users'






