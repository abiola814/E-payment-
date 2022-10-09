import email
from django.shortcuts import render, redirect
from . form import CustomUSerForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

def home(request):
    return render(request, 'landingpage.html')


def registeruser(request):
    form = CustomUSerForm()
    if request.method == 'POST':
        form = CustomUSerForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email.lower()
            user.save()
            login(request, user)
            return redirect('landing')
          
    context = {'form': form}
    return render(request, 'component/auth_modals.html', context)


def loginPage(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        email = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(email = email)

        except:
            print('user doest not exist')

        user = authenticate(email = email, password = password)


        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            print('something went wrong')

    return render(request, 'component/auth_modals.html',)


def logoutuser(request):
    logout(request)
    return redirect('login')