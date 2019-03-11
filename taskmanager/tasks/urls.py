from django.urls import path, include
from rest_framework import routers
from tasks.api import TaskViewSet

router = routers.DefaultRouter()
router.register('api/tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls))
]
