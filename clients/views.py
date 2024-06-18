from django.shortcuts import render
import random
def clients(request):
    random_number = random.randint(1, 7)
    return render(request, 'clients/index.html', context={'random_number': random_number})