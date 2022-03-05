from django.contrib.auth.decorators import login_required
from accounts.models import customUser
from .models import retinvt
from django.shortcuts import render
#
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
        'inventory' : inventory
    }
    return render(request, 'dist/static/index.html', info_dict)

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