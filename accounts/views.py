from django.shortcuts import render, HttpResponse

# Create your views here.


def signup(request):
    return render(request, 'accounts/signup.html')


def login(request):
    return render(request, 'accounts/login.html')


def forgotpassword(request):
    return render(request, 'accounts/forgot_password.html')

def profile(request):
    return render(request,'accounts/profile.html')

def edit_profile(request):
    return render(request,'accounts/edit_profile.html')

def set_new_password(request):
    return render(request, 'accounts/set_new_password.html')
