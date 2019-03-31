from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView, TeamTaskListView, TeamTaskDeleteView
from . import views

urlpatterns = [
    path('teamtask/<int:teamid>/', TeamTaskListView.as_view(),
         name='team-task-manager'),
    path('teamtask/<int:teamid>/new/',
         views.teamtaskcreate, name='team-task-create'),
    path('teamtask/<int:pk>/delete/',
         TeamTaskDeleteView.as_view(), name='team-task-delete'),
    path('', TaskListView.as_view(), name='task-manager'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task/new/', TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
]
