from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=256, unique=True)
    desc = models.CharField(max_length=256)
    assignee = models.CharField(max_length=100)
    status = models.CharField(max_length=256, blank=True)
    owner = models.ForeignKey(
        User, related_name="tasks", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
