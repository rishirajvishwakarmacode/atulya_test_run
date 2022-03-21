from django.contrib import admin
from django.urls import path
from . import views

app_name = 'products'

urlpatterns =[
    path('api/getpdt/<str:term>', views.getpdt, name='apigetpdt'),
]