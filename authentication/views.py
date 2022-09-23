from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import logout as user_logout, login as user_login
from django.contrib.messages import add_message
from django.contrib.messages import constants
# Create your views here.

def set_username(email: str, first_name: str):
    email, _ = email.split('@')
    username = f'{email}-{first_name}'
    return username

def logout(request):
    user_logout(request)
    return redirect('home')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(email = email).exists() and check_password(password, User.objects.get(email = email).password):
            user_login(request, User.objects.get(email = email))
            add_message(request, constants.SUCCESS, 'login successfully')
            return redirect('dashboard')
        else:
            add_message(request, constants.ERROR, 'Invalid credentials')
    return redirect('home')

def register(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        first_name, last_name = full_name.split(' ')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(email = email).exists():
            add_message(request, constants.ERROR, 'Email already in use')
            return redirect('home')
        else:
            u = User.objects.create_user(username= set_username(email, full_name), first_name=first_name, last_name=last_name, email=email, password=password)
            user_login(request, u)
            add_message(request, constants.SUCCESS, 'Account created successfully')
            
    return redirect('home')