from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


# Create your views here.
def login_view(request):
    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if (user):
            login(request, user)
            return redirect('index')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def signup_view(request):
    if (request.method == 'POST'):
        print(request.POST.get('username'))
        print(request.POST.get('password'))
        print(request.POST.get('confirm_password'))
        print(request.POST.get('email'))
        print(request.POST.get('firstname'))
        print(request.POST.get('lastname'))
    return render(request, 'signup.html')
