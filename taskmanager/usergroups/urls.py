from django.urls import path
from . import views

urlpatterns = [
    path('listteam/', views.list_team, name='listteam'),
    path('team/<int:pk>/', views.TeamDetail.as_view(), name='team-manager'),
    path('team/<int:teamid>/current_available/',
         views.list_available_user, name='current_available'),
    path('createteam/', views.createteam, name='create-team'),
    path('teammanager/', views.createteam, name='create-team')
]
