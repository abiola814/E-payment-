from django.urls import path, include
from . import views


urlpatterns = [
        path('', views.home, name ='home'),
        path('register/', views.registeruser, name='register'),
        path('login/', views.loginPage, name='login'),
        path('logout/', views.logoutuser, name='logout'),
        path('dashboard/', views.dashboard, name='dashboard'),
        path('general/', views.general, name='general'),
        path('licences/', views.licences, name='licences'),
        path('sales/', views.sales, name='sales'),
        path('fees/', views.fees, name='fees'),
        path('fines/', views.fines, name='fines'),
        path('services/', views.services, name='services'),
        path('activate/<uidb64>/<token>',views.activate, name='activate'),
    ]