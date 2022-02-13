from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.models import customUser
from .models import *
from .models import wholesaler_inventory as inventory_model
from .forms  import wholesaler_details_form
from products.models import Product_packed, Product_unpacked
from products.views import *

# Create your views here.
@login_required
def dashboard(request):
    try:
        user_data = customUser.objects.get(user_id = request.user.user_id)
        data = business_financial_information.objects.get(user_id_id=request.user.user_id)
        print(data)
        info_flag = data.wholesaler_business_info_complete
        context = {
            'user_name': user_data.email,
        }
    except:
        info_flag = False
    if info_flag:
        return render (request, 'wholesaler_dashboard.html', context)
    else:
        return redirect('wholesaler:fill_details')


@login_required
def connect_retailer(request):
    pass

@login_required
def fill_store_information(request):
    logged_user_id = request.user.user_id
    context = {
        'form': wholesaler_details_form()
    }

    if request.method=='POST':
        gst = request.POST['wholesale_store_gst']
        pan = request.POST['wholesale_store_pan']
        account = request.POST['wholesale_store_bank_account']
        name = request.POST['wholesale_store_name']
        ifsc = request.POST['wholesale_store_ifsc']
        upi = request.POST['wholesale_store_upi']

        save_instance = business_financial_information(user_id=customUser.objects.get(user_id = logged_user_id), PAN=pan, GSTIN=gst, IFSC=ifsc, account_number=account, beneficiary_name=name, UPI=upi, wholesaler_business_info_complete=True)
        save_instance.save()
        print ('user_details successfully filled')
        return redirect('admin')
    else:
        return render(request, 'store_information.html', context)

@login_required
def wholesaler_inventory(request):
    user = request.user.user_id
    if request.method == "GET":
        domain = inventory_model.objects.get(user_id = user)
        products = domain.packed_products.all()
        # product_list = [product for product in products.user_id ]
        # print(product_list)
        print(products)
        context = {
            'user': request.user.user_id,
            'name': request.user.email,
            'products_object': products,
        }
        return render(request, 'inventory_template.html', context)

@login_required
def add_inventory(request):
    user = request.user.user_id
    if request.method == "POST":
        search_term = request.POST['product_search']
        matching_products = search_products(request, search_term)   #from products.views
        return render(request, 'product_addition.html', {'products': matching_products})


        # return render(request, 'product_addition.html', {'loaded_products': loaded_products})

@login_required
def order_list (request): #to display order wholesaler has recived
    user = request.user.user_id
    if request.method == "GET":
        orderlist = wholesaler_order_list.objects.get(user_id = user)
        list = orderlist.packed_products.all()
        context = {
            'user': user,
            'user_email': request.user.email,
            'list' : list,
        }
        return render(request, 'order_list.html', context)
