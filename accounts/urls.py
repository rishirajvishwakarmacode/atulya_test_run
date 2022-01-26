from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name="login"),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout')
    ]