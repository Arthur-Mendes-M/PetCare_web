from django.shortcuts import render, redirect
from django.urls import reverse
from utils.API import Employees

def home(request):
    employees_list = Employees().get_all().json()

    # TODO: use this to apply pagination on employees_list
    # current_page = request.GET.get('page') if request.GET.get('page') else 0

    return render(request, 'home/index.html', context={"employees_list": employees_list})

def edit_employee(request):
    employee_id = request.GET.get('id')
    employee_data = request.GET.get('data')

    Employees().update_one(employee_id, employee_data)

    return redirect(reverse('home'))


def delete_employee(request):
    employees_id = request.GET.get('employees_id')

    Employees().delete_one(employees_id)

    return redirect(reverse('home'))