from rest_framework import serializers
from tasks.models import Task


# Task Serializers
class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('url', 'id', 'title', 'desc',
                  'assignee', 'status', 'created_at')
