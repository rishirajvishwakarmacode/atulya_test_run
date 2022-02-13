from django.contrib import admin
from django.urls import path
from . import views

app_name = 'retailer'

urlpatterns = [
    path("dashboard/", views.dashboard, name='dashboard'),
    path('fill_store_details/', views.fill_store_information, name='fill_details'),
    path('inventory/', views.retailer_inventory, name='inventory'),
    path('inventory/addtoinventory', views.add_inventory, name='add_to_inventory'),
    path('orderlist/', views.order_list, name='orderlist')

]