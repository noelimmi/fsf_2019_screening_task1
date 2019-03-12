from comments.models import Comment
from rest_framework import viewsets, permissions
from comments.serializers import CommentSerializer

# Comments Viewset


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = CommentSerializer

    # only tasks of tht authenticated user
    def get_queryset(self):
        return self.request.user.tasks.comments.all()

    # to save owner when he create task
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        serializer.save()
