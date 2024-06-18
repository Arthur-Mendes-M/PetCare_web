from django.shortcuts import render
import random 

def sales(request):
    random_number = random.randint(1, 7)
    return render(request, 'sales/index.html', context={'random_number': random_number})