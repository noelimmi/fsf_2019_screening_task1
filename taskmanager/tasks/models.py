from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
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

    @property
    def comments(self):
        queryset = Comment.objects.filter_by_instance(self)
        return queryset

    @property
    def get_content_type(self):
        task = self
        content_type = ContentType.objects.get_for_model(task.__class__)
        return content_type

    class Meta:
        ordering = ['-created_at']
        unique_together = ('title', 'owner',)

    def __str__(self):
        return self.title


class CommentManager(models.Manager):
    def filter_by_instance(self, instance):
        """ 
        Since Comment is a generic foreign key any Model class can be its instance 
        used name instance and to get its class name instance.__class__ is used
        """
        content_type = ContentType.objects.get_for_model(instance.__class__)
        object_id = instance.id
        query_set = super(CommentManager, self).filter(
            content_type=content_type, object_id=object_id)
        return query_set


class Comment(models.Model):
    user = models.ForeignKey(User, related_name="author",
                             on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    content = models.CharField(max_length=256)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = CommentManager()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return '%s-%s' % (self.user, self.content)
