from django.urls import path
from . import views

urlpatterns = [
    path('listmember/', views.list_members, name='listmember')
]
