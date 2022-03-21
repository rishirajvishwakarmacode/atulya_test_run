from django.contrib import admin
from django.urls import path
from . import views

app_name = 'retailer'

urlpatterns = [
    path('dashboard/', views.dashboard, name='retdbd'),
    path('inventory/', views.showinvt, name='retinvt'),
    path('profile/', views.showprofile, name='retprof'),
    path('searchpdt/', views.searchpdt, name='srchpdt'),
]