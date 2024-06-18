from django.shortcuts import render
import random

def user_profile(request):
    random_number = random.randint(1, 7)
    return render(request, 'user_profile/index.html', context={'random_number': random_number})