from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import customUser
from .models import *
from .models import retailer_inventory as inventory_model
from .forms  import retailer_details_form

from products.models import Product_packed, Product_unpacked

# Create your views here.
@login_required
def dashboard(request):
    try:
        user_data = customUser.objects.get(user_id = request.user.user_id)
        data = business_financial_information.objects.get(user_id_id=request.user.user_id)
        print(data)
        info_flag = data.retailer_business_info_complete
        context = {
            'user_name': user_data.email,
        }
    except:
        info_flag = False
    if info_flag:
        return render (request, 'retailer_dashboard.html', context)
    else:
        return redirect('retailer:fill_details')


@login_required
def connect_wholesaler(request):
    pass

@login_required
def fill_store_information(request):
    logged_user_id = request.user.user_id
    context = {
        'form': retailer_details_form()
    }

    if request.method=='POST':
        gst = request.POST['retail_store_gst']
        pan = request.POST['retail_store_pan']
        account = request.POST['retail_store_bank_account']
        name = request.POST['retail_store_name']
        ifsc = request.POST['retail_store_ifsc']
        upi = request.POST['retail_store_upi']

        save_instance = business_financial_information(user_id=customUser.objects.get(user_id = logged_user_id), PAN=pan, GSTIN=gst, IFSC=ifsc, account_number=account, beneficiary_name=name, UPI=upi, retailer_business_info_complete=True)
        save_instance.save()
        print ('user_details successfully filled')
        return redirect('admin')
    else:
        return render(request, 'store_information.html', context)

@login_required
def retailer_inventory(request):
    user = request.user.user_id
    if request.method == "POST":
        ptdbsrch = request.POST['product_search']
        if ptdbsrch is not None:
            products = Product_packed.objects.filter(name__contains=ptdbsrch)
            for product in products:
                product_list.append(product)
            print(product_list)
    if request.method == "GET":
        products = inventory_model.objects.filter(user_id = user)
        print(products)
        context = {
            'user': request.user.user_id,
            'name': request.user.email,
            'products_object': products,
        }
        return render(request, 'inventory_template.html', context)