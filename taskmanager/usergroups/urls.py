from django.urls import path
from . import views

urlpatterns = [
    path('listteam/', views.list_team, name='listteam'),
    path('team/<int:pk>/', views.TeamDetail.as_view(), name='team-manager'),
    path('createteam/', views.createteam, name='create-team'),
    path('team/<int:pk>/update/', views.TeamUpdateView.as_view(), name='update-team'),
    path('team/<int:pk>/delete/', views.TeamDeleteView.as_view(), name='delete-team'),
    path('team/<int:userid>/<int:teamid>/<str:operation>/',
         views.change_teammember, name='changeteammember')
]
