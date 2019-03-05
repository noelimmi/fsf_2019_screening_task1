from rest_framework import serializers
from .models import Task


# Task Serializers
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
