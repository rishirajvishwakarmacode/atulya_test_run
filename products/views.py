from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# Create your views herem


@login_required
def search_products(request, name):
    return (Product_packed.objects.filter(name__icontains=name))

@staff_member_required
def add_product(request, list):
    pass


