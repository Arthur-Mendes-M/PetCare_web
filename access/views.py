from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from dotenv import load_dotenv

from utils.session_handler import session_handler
from utils.API import Employees

# Load environment variables from .env file
load_dotenv()

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
       
        api_response = Employees().validate({'email': email, 'password': password})
        api_data = api_response.json()

        if api_response.status_code == 200:
            session_handler(request, 'employee', api_data[0], 'set')
            response = redirect(reverse('home'))
        else:
            messages.error(request, api_data['description'])
            response = render(request, 'login.html')
            
        return response

    return render(request, 'login.html')

def signup(request):    
    if request.method == 'POST':
        data = {
            "name": request.POST.get('name'),
            "email": request.POST.get('email'),
            "password": request.POST.get('password'),
            "role": request.POST.get('role')
        }

        file = {
            'image': request.FILES['image'] if request.FILES and request.FILES['image'] else None
        }
    
        Employees().save_one(data=data, files=file)

        return redirect(reverse('login'))

    return render(request, 'signup.html')

def logout(request):
    session_handler(request, 'employee', None, 'delete')

    return redirect(reverse('login'))