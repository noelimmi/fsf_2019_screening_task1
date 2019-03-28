from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm

urlpatterns = [
    path('register/', views.register, name='user-register'),
    path('profile/', views.profile, name='user-profile'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', authentication_form=UserLoginForm),
         name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'),
         name='user-logout'),
]
