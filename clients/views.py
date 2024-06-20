from django.shortcuts import render, redirect
from django.urls import reverse
from utils.API import Clients
from utils.datetime import format_date
import random
import json
import os

from django.views.decorators.csrf import csrf_exempt

def clients(request):
    random_number = random.randint(1, 7)
    clients_list = Clients().get_all().json()

    for client in clients_list:
        client['birthday_formatted'] = format_date(client['birthday'], type="date")

    return render(request, 'clients/index.html', context={'clients_list': clients_list, 'random_number': random_number, "api_url": f"{os.getenv('PETCARE_API_URL')}clients", "api_token": f"?auth={os.getenv('PETCARE_AUTH_TOKEN')}"})

def create_client(request): 
    files = request.FILES if (request.FILES and 'image' in request.FILES) else None
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    birthday = request.POST.get('birthday')
    cep = request.POST.get('cep')
    neighborhood = request.POST.get('neighborhood')
    street = request.POST.get('street')
    number = request.POST.get('street_number')
    state = request.POST.get('state')
    city = request.POST.get('city')

    client = {
        "name": name,
        "email": email,
        "password": password,
        "birthday": birthday,
        "address": json.dumps({
            "cep": cep,
            "neighborhood": neighborhood,
            "street": street,
            "street_number": number,
            "state": state,
            "city": city
        })
    }

    Clients().save_one(data=client, files=files)

    return redirect(reverse('clients'))

@csrf_exempt
def edit_client(request):
    files = request.FILES if (request.FILES and 'image' in request.FILES) else None
    client_id = request.POST.get('id')
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    birthday = request.POST.get('birthday')
    cep = request.POST.get('cep')
    neighborhood = request.POST.get('neighborhood')
    street = request.POST.get('street')
    number = request.POST.get('street_number')
    state = request.POST.get('state')
    city = request.POST.get('city')

    client = {
        "name": name,
        "email": email,
        "password": password,
        "birthday": birthday,
        "address": json.dumps({
            "cep": cep,
            "neighborhood": neighborhood,
            "street": street,
            "street_number": number,
            "state": state,
            "city": city
        })
    }

    Clients().update_one(client_id, client, files)

    return redirect(reverse('clients'))


@csrf_exempt
def delete_client(request):
    clients_id = request.GET.get('clients_id')
    id_list = None

    if clients_id and ',' in clients_id:
        id_list = clients_id.split(',')

    if id_list != None:
        for id in id_list:
            Clients().delete_one(id)
    else:
        Clients().delete_one(clients_id)

    return redirect(reverse('clients'))