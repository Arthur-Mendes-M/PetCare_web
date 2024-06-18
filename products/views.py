from django.shortcuts import render
import random

def products(request):
    random_number = random.randint(1, 7)
    return render(request, 'products/index.html', context={"random_number": random_number})