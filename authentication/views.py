from logging import exception
from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import logout as user_logout, login as user_login
from django.contrib.messages import add_message ,constants
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .email_token import account_activation_token
from django.conf import settings
# Create your views here.

def activate(request, uidb64, token):

    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        add_message(request,constants.SUCCESS, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('home')
    else:
        add_message(request,constants.ERROR, "Activation link is invalid!")

    return redirect('home')

def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    print(user.username)
    print(to_email)
    email = EmailMessage(subject=mail_subject, body=message,from_email=settings.EMAIL_FROM_USER, to=[to_email])
    if email.send(fail_silently = False):
        add_message(request,constants.SUCCESS, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
                received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        add_message(request,constants.ERROR, f'Problem sending email to {to_email}, check if you typed it correctly.')

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

        try:
            first_name, last_name = full_name.split(' ')
        except ValueError:
            add_message(request, constants.ERROR, 'please input your full name with space ')
            return redirect('home')

        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(email = email).exists():
            add_message(request, constants.ERROR, 'Email already in use')
            return redirect('home')
        else:
            u = User.objects.create_user(username= set_username(email, full_name),is_active=False, first_name=first_name, last_name=last_name, email=email, password=password)
            activateEmail(request, u, email)
            
    return redirect('home')