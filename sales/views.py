from django.shortcuts import render, HttpResponse
from utils.API import Products, Clients, Sales
import random

def sales(request):
    random_number = random.randint(1, 7)

    products_list = Products().get_all().json()
    clients_list = Clients().get_all().json()

    return render(request, 'sales/index.html', context={'random_number': random_number, 'products_list': products_list, 'clients_list': clients_list})

def create_sale(request):
    random_number = random.randint(1, 7)


    products_list = Products().get_all().json()
    clients_list = Clients().get_all().json()

    products = request.POST.getlist('product[]')
    products_quantity = request.POST.getlist('quantity[]')
    client_id = request.POST.get('client')
    payment_method = request.POST.get('payment_method')

    sold_products = [{"quantity": int(products_quantity[i]), "product_id": int(products[i])} for i in range(len(products))]

    sold_saved = Sales().save_one({
        "client_id": int(client_id),
        "payment_method": payment_method,
        "products": sold_products
    }).json()

    if isinstance(sold_saved, list) and len(sold_saved) > 0:
        return render(request, 'sales/index.html', context={'random_number': random_number, "sale_was_created": "true", 'products_list': products_list, 'clients_list': clients_list})
    else:
        return render(request, 'sales/index.html', context={'random_number': random_number, "sale_was_created": "false", 'products_list': products_list, 'clients_list': clients_list})