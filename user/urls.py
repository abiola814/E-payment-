from django.urls import path, include
from . import views


urlpatterns = [
        path('', views.home, name ='landing'),
        path('register/', views.registeruser, name='register'),
        path('login/', views.loginPage, name='login'),
        path('logout/', views.logoutuser, name='logout'),
    ]