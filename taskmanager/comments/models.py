from django.db import models
from tasks.models import Task
from django.contrib.auth.models import User


class Comment(models.Model):
    user = models.ForeignKey(User, related_name="author",
                             on_delete=models.CASCADE)
    task = models.ForeignKey(User, related_name="task",
                             on_delete=models.CASCADE)
    content = models.CharField(max_length=256)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
