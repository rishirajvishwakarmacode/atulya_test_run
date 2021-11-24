from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("")
firebase_admin.initialize_app(cred)

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST.get('username_field')
        password = request.POST.get('password_field')
        print(username)
        print(password)

    return render(request, 'login2.html')

