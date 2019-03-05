from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=256, unique=True)
    desc = models.CharField(max_length=256)
    assignee = models.CharField(max_length=100)
    status = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
