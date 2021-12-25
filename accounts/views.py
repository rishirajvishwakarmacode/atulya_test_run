from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
import firebase_admin
from firebase_admin import credentials, auth
import pyrebase
#================================initialisation with firebase-admin ============================

cred = credentials.Certificate("keys/testproject-310ca-firebase-adminsdk-1nyyo-47ba9fd115.json")
firebase_admin.initialize_app(cred)

#================================initialization of firebase with firebase =========================

firebase_config ={
    'apiKey': "AIzaSyChMeMsww5jTKuisGI8R91baVB9NPuauwY",
    'authDomain': "testproject-310ca.firebaseapp.com",
    'projectId': "testproject-310ca",
    'storageBucket': "testproject-310ca.appspot.com",
    'messagingSenderId': "744873412899",
    'appId': "1:744873412899:web:4a6bd5c1bfc2017322e496",
    'measurementId': "G-VGDGX0ZP9V",
    'databaseURL': 'https://testproject-310ca-default-rtdb.firebaseio.com/'
}

firebase_app = pyrebase.initialize_app(firebase_config)
auth_instance = firebase_app.auth()  # Authorisation instance
#===================================================================================

def register(request):
    if request.method == "POST":
        registeration_mail = request.POST.get('registeration_email')
        registeration_password = request.POST.get('registeration_password')
        registeration_phone_number = request.POST.get('registeration_phone_number')
        created_user = firebase_admin.auth.create_user(
            email= registeration_mail,
            email_verified = False,
            password = registeration_password
        )
        print('user registration successful')
        print(created_user)
    else:
        return render(request, 'userregisteration.html')
    return render(request, 'userregisteration.html')


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST.get('username_field')
        password = request.POST.get('password_field')
        try:
            logged_in_user = auth_instance.sign_in_with_email_and_password(username, password)
            print(logged_in_user)

        except:
            print("login failed")
    return render(request, 'login2.html')

#=================================== get_user_data ================================================================

def getdata(request):
    user = firebase_admin.auth.get_user_by_email('coderishiraj@gmail.com')
    return render (request, 'userdata.html', {'userdata': user})

#======================================user data =================================================================
'''class human():
    def __init__(self, name, mobile_number, email, upiaddress):
        self.name = name
        self.mobile_number = mobile_number
        self.email = email
        self.upiaddress = upiaddress

    def get_user_data(self, email):
        user_data = firebase_admin.auth.get_user_by_email(email)
        return (user_data)

class buyers(human):
    def __init__(self):
        pass

    def metadata(self):
        pass

'''

class logged_in_user():
    def __init__(self, kind, localId, email, displayName, idToken, registrered, refreshToken ):
        self.kind = kind
        self.localId = localId
        self.email = email
        self.displayName
        self.idToken = idToken
        self.registered = registrered
        self.refeshToken = refreshToken











