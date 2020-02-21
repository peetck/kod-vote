from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def login_view(request):
    form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'login.html', context)

def signup_view(request):
    form = UserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'signup.html', context)