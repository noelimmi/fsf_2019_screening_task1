from django.db import models
from django.contrib.auth.models import User
from usergroups.models import Team
from django.urls import reverse


class Task(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(
        max_length=512, blank=True, null=True)
    assignee = models.ManyToManyField(
        User, related_name="assignee_mtem", blank=True)
    status_choices = (('pl', 'Planned'), ('ip', 'In Progress'),
                      ('do', 'Done'), ('st', 'Started'),)
    status = models.CharField(
        max_length=2, choices=status_choices, default='pl')
    owner = models.ForeignKey(
        User, related_name="tasks", on_delete=models.CASCADE, null=True, blank=True)
    team = models.ForeignKey(
        Team, related_name="teamtasks", on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('title', 'owner',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    user = models.ForeignKey(User, related_name="author",
                             on_delete=models.CASCADE)
    teamtask = models.ForeignKey(Task, related_name="taskcomments",
                                 on_delete=models.CASCADE, null=True, blank=True)
    content = models.CharField(max_length=256)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return '%s:%s' % (self.user, self.content)
