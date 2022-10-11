import email
from django.shortcuts import render, redirect

from user.models import Profile
from . form import CustomUSerForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .email_token import account_activation_token
from django.conf import settings
from django.contrib.messages import add_message ,constants

def activate(request, uidb64, token):
    """
    Get request.
    activation of your account
    :param request:
    :param user uid:
    :param token generated
    :return: route
    """

    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('general')
    else:
        add_message(request,constants.ERROR, "Activation link is invalid!")

    return redirect('home')

def activateEmail(request, user, to_email):

    """
    Get request.
    send email to user for activation
    :param request:
    :param User object:
    :param email
    :return: mail
    """
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


def home(request):
    return render(request, 'landingpage.html')


def registeruser(request):
    # form = CustomUSerForm()
    if request.method == 'POST':
        username = request.POST['email'].lower()
        email = request.POST['email'].lower()
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        profile_image = request.FILES.get('filename')


        # This can be rendered out as an error message
        if password1 != password2:
            print('invalid password match')
            add_message(request,constants.ERROR, f'invalid password matc')


        elif len(password1) < 8:
            print('Try a stronger password')
            add_message(request,constants.ERROR, f'Try a stronger password')
        
        else:
            user = User.objects.create_user(username=username, password=password1, first_name=first_name,last_name=last_name, email=email,)
            user.is_active = False
            user.save()
            # login(request, user)
            print("user created")

# Makes a profile everytime a user is created
            Profile.objects.create(
                user = user,
                full_name = first_name + " " + last_name,
                email = email,
                profile_image = profile_image
            )
            # print('success')
            activateEmail(request, user, email)
            return redirect('home')

          

    return render(request, 'landingpage.html', )


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('email').lower()
        password = request.POST.get('password')

        print(username)

        try:
            user = User.objects.get(username = username)

        except:
            print('user doest not exist')
            add_message(request,constants.ERROR, f'user doest not exist')


        user = authenticate(username = username, password = password)


        if user is not None:
            print(username, password)
            login(request, user)
            return redirect('general')


        else:
            print('something went wrong')
            print(username)
          

    return render(request, 'landingpage.html')


def logoutuser(request):
    print('logging out')
    logout(request)
    return redirect('login')


def dashboard(request):
    return render(request, 'dashboard.html')


def general(request):
    return render(request, 'general.html',)


def licences(request):

    return render(request, 'licenses.html',)


def fines(request):
    return render(request, 'fines.html')



def fees(request):
    return render(request, 'fees.html')


def sales(request):
    return render(request, 'sales.html')


def services(request):
    return render(request, 'services.html')