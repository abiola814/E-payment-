from django.shortcuts import render


def home(request):
    return render(request,'landingpage.html')

def about(request):
    return render(request, 'about.html')

def terms_and_condition(request):
    return render(request, 'terms.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def services(request):
    return render(request, 'services.html')
def connect(request):
    return render(request, 'connector.html')