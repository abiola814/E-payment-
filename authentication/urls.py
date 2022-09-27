from django.urls import path
from .views import login, logout, register,activate


app_name = 'auth'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('activate/<uidb64>/<token>',activate, name='activate')

]