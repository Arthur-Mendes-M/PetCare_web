from django.shortcuts import render, redirect
from django.urls import reverse
from utils.API import Employees
import random
from utils.session_handler import session_handler

def user_profile(request):
    random_number = random.randint(1, 7)
    return render(request, 'user_profile/index.html', context={'random_number': random_number})

def edit_profile(request):
    employee_id = request.GET.get('employee_id')
    
    file = request.FILES if (request.FILES and 'image' in request.FILES) else None

    employee = {
        "name": request.POST.get('name'),
        "email": request.POST.get('email')
    }

    if file:
        employee = Employees().update_one(employee_id, employee, file).json()[0]
    else:
        employee = Employees().update_one(employee_id, employee).json()[0]

    session_handler(request, 'employee', employee, 'set')

    return redirect(reverse('user_profile'))