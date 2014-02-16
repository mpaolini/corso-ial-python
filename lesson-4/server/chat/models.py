from django.db import models


class ChatMessage(models.Model):
    text = models.TextField()
    username = models.CharField(max_length=100)
