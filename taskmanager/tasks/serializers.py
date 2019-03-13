from rest_framework import serializers
from tasks.models import Task, Comment


# Task Serializers
class TaskSerializer(serializers.ModelSerializer):
    taskcomments = serializers.StringRelatedField(many=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'desc',
                  'assignee', 'status', 'taskcomments')


class CommentSerializer(serializers.ModelSerializer):
    task = serializers.PrimaryKeyRelatedField

    class Meta:
        model = Comment
        fields = ('id', 'task', 'content')
