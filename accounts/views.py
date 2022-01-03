import django.contrib.auth
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from accounts.models import customUser
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

def login(request):
    if request.method == 'POST':
        email= request.POST['login_email']
        # print(email)
        password = request.POST['login_password']
        # print(password)
        user = authenticate(username = email, password = password)
        if user is not None:
            auth_login(request, user)
            print('user logged in successfully')
        else:
            print("user is not logged in")
    return render(request, 'login.html')

def logout(request):
    django.contrib.auth.logout(request, user)

def register(request):
    if request.method == 'POST':
        email = request.POST['registration_email']
        type = request.POST['type']
        password = request.POST['password_field']
        user = customUser.objects.create_user(email, type, password)
        user.save()

        print('user created successfully')
        return redirect ("{% url 'accounts:login'%}")
    return render(request, 'registrationform.html')











