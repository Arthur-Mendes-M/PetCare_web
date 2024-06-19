from django.shortcuts import render
from utils.API import Clients
import random

def clients(request):
    random_number = random.randint(1, 7)
    clients_list = Clients().get_all().json()

    return render(request, 'clients/index.html', context={'clients_list': clients_list, 'random_number': random_number})