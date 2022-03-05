from retailer.models import *
# from manufacturer.models import *
from django.shortcuts import render
import retailer.models as RTmodels
import wholesaler.models as WRmodels
# import manufacturer.models as MRmodels
from products.views import *
from accounts.models import customUser
# from orders.models import RTWS_orders, WSMR_orders, CSRT_order




def get_info(request, user):
    if user.type == 'retailer':
        info_dict = {
            'type' : 'retailer',
            'querymodel' : RTmodels,
            'invt_model' : RTmodels.retailer_inventory,
            'info_model' : RTmodels.business_financial_information,
            'order_model' : RTmodels.retailer_order_list
        }
    elif user.type == 'wholesaler':
        info_dict = {
            'type' : 'wholesaler',
            'querymodel' : WRmodels,
            'invt_model' : WRmodels.WRinventory,
            'info_model' : WRmodels.WRBI,
        }
    return (info_dict)

def get_product_inf(request, uuid):
    pass



def get_inventory(request, user):
    user_info = get_info(request, user)
    model = user_info['invt_model']
    print(model)
    domain = model.objects.get(user_id = user.user_id)
    print(domain)
    products = domain.products.all()
    context = {
        'user': user.user_id,
        'name': user.email,
        'products_object': products,
    }
    return (context)



    '''if user.type == 'retailer':
        domain = model.retailer_inventory.objects.get(user_id = user.user_id)
        products = domain.packed_products.all()
        context = {
            'user': user.user_id,
            'name': user.email,
            'products_object': products,
        }
    elif user.type == 'wholesaler':
        domain = model.WRinventory.objects.get(user_id = user.user_id)
        products = domain.packed_products.all()
        context = {
            'user': user.user_id,
            'name': user.email,
            'products_object': products,
        }
    return (context)'''

def search (request, user):
    model = querymodel(request, user)
    if request.method == "POST":
        search_term = request.POST['term']
        products = search_products(request, search_term)  # at product.views
        context = {
            'products':products
        }
        return (context)

def get_orders(request, user):
    pass

def connect(request, user1, user2):
    pass

# def get_orderquery(request, receiver_id, sender_id):
#     receiver = customUser.objects.get(user_id = receiver_id)
#     sender = customUser.objects.get(user_id = sender_id)
#     if receiver.type == 'wholesaler' and sender.type =='retailer':
#         model = RTWS_orders
#     elif receiver.type == 'manufacturer' and sender.type =='wholesaler':
#         model = WSMR_orders
#     elif receiver.type == 'retailer' and sender.type =='consumer':
#         pass
#
#     return (model)

def add_to_inventory(request, user, products):
    model_dict = get_info(request, user)
    user_domain = model_dict['invt_model'].objects.get(user_id = user.user_id)
    for product in products:
        user_domain.products.add(product)
        print(product + 'added Succefully')

def delete_item(request, user, item):
    pass

def update_item(request, user, item, update):
    pass

def place_order(request, sender, reciever, order_list):
    pass




