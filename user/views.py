import email
from django.shortcuts import render, redirect

from user.models import Profile
from . form import CustomUSerForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

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
        profile_image = request.POST['filename']


        # This can be rendered out as an error message
        if password1 != password2:
            print('invalid password match')

        elif len(password1) < 8:
            print('Try a stronger password')
        
        else:
            user = User.objects.create_user(username=username, password=password1, first_name=first_name,last_name=last_name, email=email,)
            user.save()
            login(request, user)
            print("user created")

# Makes a profile everytime a user is created
            Profile.objects.create(
                user = user,
                full_name = first_name + " " + last_name,
                email = email,
                profile_image = profile_image
            )
            print('success')
            return redirect('general')
          

    return render(request, 'landingpage.html', )


def loginPage(request):

    # page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST['email'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username = username)

        except:
            print('user doest not exist')

        user = authenticate(username = username, password = password)


        if user is not None:
            login(request, user)
            # print(username, password)
            return redirect('general')


        else:
            print('something went wrong')
            # print(username)
            # print(password)

    return render(request, 'landingpage.html')


def logoutuser(request):
    print('logging out')
    logout(request)
    return redirect('login')


def dashboard(request):
    return render(request, 'dashboard.html')


def general(request):
    profile = request.user.profile
    return render(request, 'general.html', {'profile': profile})