from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from utils.API import Employees

def home(request):
    employees_list = Employees().get_all().json()

    # TODO: use this to apply pagination on employees_list
    # current_page = request.GET.get('page') if request.GET.get('page') else 0

    return render(request, 'home/index.html', context={"employees_list": employees_list})

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
