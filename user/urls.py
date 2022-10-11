from django.urls import path, include
from . import views


urlpatterns = [
        path('', views.home, name ='home'),
        path('register/', views.registeruser, name='register'),
        path('login/', views.loginPage, name='login'),
        path('logout/', views.logoutuser, name='logout'),
        # path('dashboard/', views.dashboard, name='dashboard'),
        path('general/', views.general, name='general'),
    ]