from django.shortcuts import render

# Create your views here.
def login_view(request):
    if (request.method == 'POST'):
        print(request.POST.get('username'))
        print(request.POST.get('password'))
    return render(request, 'login.html')

def signup_view(request):
    return render(request, 'signup.html')