from django.shortcuts import render, redirect
from django.urls import reverse
from utils.API import Employees
import random

def home(request):
    random_number = random.randint(1, 7)
    employees_list = Employees().get_all().json()

    # TODO: use this to apply pagination on employees_list
    # current_page = request.GET.get('page') if request.GET.get('page') else 0

    return render(request, 'home/index.html', context={"employees_list": employees_list, "random_number": random_number})

def create_employee(request): 
    files = request.FILES if (request.FILES and 'image' in request.FILES) else None
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    role = request.POST.get('role')

    employee = {
        "name": name,
        "email": email,
        "password": password,
        "role": role if role else None
    }

    Employees().save_one(data=employee, files=files)

    return redirect(reverse('home'))

def edit_employee(request):
    employees_id = request.GET.get('employees_id')
    id_list = None

    employee = {
        "name": request.GET.get('name'),
        "email": request.GET.get('email'),
        "role": request.GET.get('role')
    }

    if ',' in employees_id:
        id_list = employees_id.split(',')

    if id_list != None:
        for id in id_list:
            Employees().update_one(id, employee)
    else:
        Employees().update_one(employees_id, employee)

    return redirect(reverse('home'))


def delete_employee(request):
    employees_id = request.GET.get('employees_id')
    id_list = None

    if ',' in employees_id:
        id_list = employees_id.split(',')

    if id_list != None:
        for id in id_list:
            Employees().delete_one(id)
    else:
        Employees().delete_one(employees_id)

    return redirect(reverse('home'))
