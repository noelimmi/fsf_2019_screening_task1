from tasks.models import Task
from rest_framework import viewsets, permissions
from tasks.serializers import TaskSerializer

# Task Viewset


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TaskSerializer

    # only tasks of tht authenticated user
    def get_queryset(self):
        return self.request.user.tasks.all()

    # to save owner when he create task
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
