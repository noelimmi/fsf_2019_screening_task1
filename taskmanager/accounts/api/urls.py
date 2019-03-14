from django.urls import path, include
from apiviews import RegisterAPI, LoginAPI, UserAPI
from knox import views as Knox_views

urlpatterns = [
    path('auth/auth', include('knox.urls')),
    path('api/auth/register', RegisterAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view()),
    path('api/auth/user', UserAPI.as_view()),
    path('api/auth/logout', Knox_views.LogoutView.as_view(), name='Knox_logout')
]