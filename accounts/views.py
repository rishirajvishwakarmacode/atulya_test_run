import django.contrib.auth
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from accounts.models import customUser
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required


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
            user_info = customUser.objects.get(email = email)
            print(user_info)
            if user_info.type == 'retailer':
                return redirect('retailer:retdbd')
                print('user_looged in to the retailer section')
            elif user_info.type == 'wholesaler':
                return redirect('wholesaler:dashboard')
            elif user_info.type == 'manufacturer':
                return redirect('manufacturer:dashboard')
            else:
                print ("user type not defined please define one")
                return redirect('accounts:login')

        else:
            print("user is not logged in")
    return render(request, 'login.html')

@login_required
def logout(request):
    django.contrib.auth.logout(request)
    print('user logged out successfully')
    return redirect ('accounts:login')

def register(request):
    if request.method == 'POST':
        email = request.POST['registration_email']
        type = request.POST['type']
        password = request.POST['password_field']
        user = customUser.objects.create_user(email, type, password)
        user.save()
        print('user created successfully')
        return redirect ('accounts:login')
    return render(request, 'registrationform.html')


def change_password(self, user_id):
    pass

def change_email(self, user_id):
    pass











