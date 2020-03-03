from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from polls.models import Poll
import datetime

# Create your views here.
def login_view(request):
    context = {}
    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if (user):
            login(request, user)
            next_url = request.POST.get('next_url')
            if (next_url != 'None'):
                return redirect(next_url)
            else:
                return redirect('index')
        context['error'] = 'error'
    next_url = request.GET.get('next')
    context['next_url'] = next_url
    return render(request, 'login.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')

def signup_view(request):
    context = {}
    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        email = request.POST.get('email')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')

        if (User.objects.filter(username=username).exists()):
            context['error'] = 'Username has already been taken!!'
            return render(request, 'signup.html', context)
        if (password == confirm_password):
            user = User.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
                email=email
            )
            login(request, user)
            return redirect('index')
        context['error'] = 'Password doesn\'t match!!'
    return render(request, 'signup.html', context)


@login_required
def my_polls_view(request):
    context = {}
    polls = Poll.objects.filter(create_by=request.user).order_by('-start_date')
    context['polls'] = polls
    context['now'] = datetime.datetime.now()
    return render(request, 'mypolls.html', context)
