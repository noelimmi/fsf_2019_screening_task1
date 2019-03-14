from django.urls import path, include
from rest_framework import routers
from tasks.api.viewsapi import TaskViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register('api/tasks', TaskViewSet, 'tasks')
router.register('api/comments', CommentViewSet, 'comment')

urlpatterns = [
    path('', include(router.urls))
]
