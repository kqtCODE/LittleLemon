from django.urls import path
from rest_framework.authtoken import views
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.signup_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('api-token-auth', views.obtain_auth_token)
]
