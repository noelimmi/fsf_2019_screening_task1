from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView, TeamTaskListView
from . import views

urlpatterns = [
    path('', TaskListView.as_view(), name='task-manager'),
    path('teamtask/<int:teamid>/', TeamTaskListView.as_view(),
         name='team-task-manager'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task/new/', TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
]
