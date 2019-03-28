from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=512, blank=True, default="")
    assignee = models.CharField(max_length=100, default="")
    status = models.CharField(max_length=256, blank=True)
    owner = models.ForeignKey(
        User, related_name="tasks", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('title', 'owner',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, related_name="author",
                             on_delete=models.CASCADE)
    task = models.ForeignKey(Task, related_name="taskcomments",
                             on_delete=models.CASCADE, null=True, blank=True)
    content = models.CharField(max_length=256)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return '%s:%s' % (self.user, self.content)
