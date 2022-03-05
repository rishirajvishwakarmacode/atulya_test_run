import retailer.views
from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from retailer.views import getinfo
# Create your views here.

@login_required
def getinfo(request):
    user = retailer.views.getinfo(request)
    return(user)

@login_required
def dashboard(request):
    return render(request, 'dist/static/index.html')

@login_required
def getinvt(request):
    user = getinfo(request)
    domain = wslinvt.objects.get(user_id = user.user_id)
    invt = domain.packed_products.all()
    return(invt)

@login_required
def showinvt(request):
    inventory = getinvt(request)
    invt_dict = {
        'inventory' : inventory
    }
    return render(request, 'inventory_template.html', invt_dict)

@login_required
def showprofile(request):
    return render(request, 'dist/static/pages-profile.html')

@login_required
def addpdt(request):
    pass

@login_required
def showorders(request):
    pass