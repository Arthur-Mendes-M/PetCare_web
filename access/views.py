from django.shortcuts import render, redirect
from django.urls import reverse
from dotenv import load_dotenv

from utils.session_handler import session_handler
from utils.API import Employees

import ast

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
            response = render(request, 'login.html', {'login_error': api_data['description']})
            
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
    
        # TEMP
        Employees().save_one(data=data, files=file)

        # UPDATE THE LOGIC BELOW - SIMPLIFY
        # FIX THE PROBLEMS
        # response = Employees().save_one(data=data, files=file)
        # response_to_obj = ""

        # if 'error' in response.json():
        #     response_to_obj = ast.literal_eval(response.json()["error"])
        # elif 'description' in response.json() and 'megabytes' in response.json()['description']:
        #     return render(request, 'signup.html', {"signup_error": "Imagem muito grande. Utilize imagens de até 3M e com extensões .jpeg, .jpg ou .png"})

        # if 'code' in response_to_obj and response_to_obj['code'] == '23505':
        #     return render(request, 'signup.html', {"signup_error": "Esse e-mail já existe! Utilize outro."})


        return redirect(reverse('login'))

    return render(request, 'signup.html')

def logout(request):
    session_handler(request, 'employee', None, 'delete')

    return redirect(reverse('login'))