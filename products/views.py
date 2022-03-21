from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .serializer import ppdtSerializer
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
# Create your views herem


@login_required
def search_products(request, name):
    return (Product_packed.objects.filter(name__icontains=name))

@login_required
def get_pdt_id(request, id):
    return(Product_packed.objects.filter(id=id))

@login_required
def get_pdt_name(request, name):
    pass

@staff_member_required
def add_product(request):
    pass


# ========================================================= API functions ================================================
def getpdt(request, term):
    queryset = Product_packed.objects.filter(name__icontains=term)
    print(queryset)
    serializer = ppdtSerializer(queryset, many=True)
    print(serializer.data)
    return JsonResponse(serializer.data, safe=False)

def getpdtbyid(request, id):
    product = Product_packed.objects.get(id=id)
    print(product)
    # return(product)
    serializer = ppdtSerializer(product)
    return JsonResponse(serializer.data, safe=True)




