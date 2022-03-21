import products.views
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from accounts.models import customUser
from .models import retinvt
from django.shortcuts import render
from products.views import search_products, getpdt
from django.http import HttpResponse, JsonResponse
from .forms import addproductForm

@login_required
def getinfo(request):
    user = customUser.objects.get(user_id = request.user.user_id)
    print('user fetched successfully')
    print(user)
    return(user)

@login_required
def dashboard(request):
    inventory = getinvt(request)
    print(inventory)
    info_dict = {
        'inventory' : inventory,

    }
    return render(request, 'basedboard.html', info_dict)

@login_required
def getinvt(request):
    user = getinfo(request)
    domain = retinvt.objects.get(user_id = user.user_id)
    invt = domain.packed_products.all()
    return(invt)

@login_required
def showinvt(request):
    inventory = getinvt(request)
    invt_dict = {
        'inventory' : inventory,
        'addpdtform': addproductForm
    }
    print(invt_dict)
    return render(request, 'rinvttemplate.html', invt_dict)

@login_required
def showprofile(request):
    return render(request, 'dist/static/pages-profile.html')

@login_required
def searchpdt(request):
    if request.method == "POST":
        term = request.POST['searchterm']
        print(term)
        return(getpdt(request, term))

@login_required
def addpdt(request):
    if request.method == "POST":
        id = request.POST['pdtid']
        sellprice = request.POST['sellprice']
    user = getinfo(request)
    domain = retinvt.objects.filter(use_id = user.user_id)
    product = products.views.get_pdt_id(request, id)
    domain.packed_products.add(product, through_defaults = {'available':True, 'sellprice':sellprice})

@login_required
def showorders(request):
    pass