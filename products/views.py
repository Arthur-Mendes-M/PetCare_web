from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from utils.API import Products
from utils.datetime import format_date
from django.views.decorators.csrf import csrf_exempt

import random
import os

def products(request):
    random_number = random.randint(1, 7)
    products_list = Products().get_all().json()

    for product in products_list:
        product["last_refill_formatted"] = format_date(product["last_refill"])

    return render(request, 'products/index.html', context={"products_list": products_list, "random_number": random_number, "api_url": f"{os.getenv('PETCARE_API_URL')}products", "api_token": f"?auth={os.getenv('PETCARE_AUTH_TOKEN')}"})

def create_product(request): 
    files = request.FILES if (request.FILES and 'image' in request.FILES) else None
    name = request.POST.get('name')
    description = request.POST.get('description')
    quantity_in_stock = request.POST.get('quantity_in_stock')
    sale_price = request.POST.get('sale_price')
    purchase_price = request.POST.get('purchase_price')

    product = {
        "name": name,
        "description": description,
        "quantity_in_stock": quantity_in_stock,
        "sale_price": sale_price,
        "purchase_price": purchase_price
    }

    Products().save_one(data=product, files=files)

    return redirect(reverse('products'))

@csrf_exempt
def edit_product(request):
    product_id = request.POST.get('id')
    files = request.FILES if (request.FILES and 'image' in request.FILES) else None
    name = request.POST.get('name')
    description = request.POST.get('description')
    quantity_in_stock = request.POST.get('quantity_in_stock')
    sale_price = request.POST.get('sale_price')
    purchase_price = request.POST.get('purchase_price')

    product = {
        "name": name,
        "description": description,
        "quantity_in_stock": quantity_in_stock,
        "sale_price": sale_price,
        "purchase_price": purchase_price
    }

    Products().update_one(product_id, product, files)

    return redirect(reverse('products'))

@csrf_exempt
def delete_product(request):
    products_id = request.GET.get('products_id')
    id_list = None

    if products_id and ',' in products_id:
        id_list = products_id.split(',')

    if id_list != None:
        for id in id_list:
            Products().delete_one(id)
    else:
        Products().delete_one(products_id)

    return redirect(reverse('products'))
