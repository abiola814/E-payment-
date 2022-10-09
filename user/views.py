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
    return render(request, 'user/verify.html', context)


def loginPage(request):

    # page = 'login'

    if request.user.is_authenticated:
        return redirect('landing')

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
            return redirect('landing')


        else:
            print('something went wrong')
            # print(username)
            # print(password)

    return render(request, 'landingpage.html')


def logoutuser(request):
    print('logging out')
    logout(request)
    return redirect('login')