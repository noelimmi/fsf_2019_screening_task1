from tasks.models import Task
from rest_framework import viewsets, permissions
from tasks.serializers import TaskSerializer

# Task Viewset


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TaskSerializer
