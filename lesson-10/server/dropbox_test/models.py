from django.db import models


class DropboxUser(models.Model):
    access_token = models.CharField(max_length=1024)
    user_id = models.IntegerField()


class DropboxCode(models.Model):
    code = models.CharField(max_length=2048)
