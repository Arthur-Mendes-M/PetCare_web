from django.shortcuts import render, redirect
from django.urls import reverse
import json
import requests
# Create your views here.

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def login(request):
    if request.method == 'POST':
        # verify is user exists
        email = request.POST.get('email')
        password = request.POST.get('password')


        # TODO: split the API logics in other files
        petcare_validate_employee_url = f"{os.getenv('PETCARE_API_URL')}employees/?auth={os.getenv('PETCARE_AUTH_TOKEN')}"
        petcare_validate_headers = {
            'Content-Type': 'application/json'
        }
        petcare_validate_content_data = json.dumps({
            'email': email,
            'password': password
        })

        response = requests.get(petcare_validate_employee_url, headers=petcare_validate_headers, data=petcare_validate_content_data)
        validated_user_data = response.json()

        if response.status_code == 400:
            response = render(request, 'login.html', context={"user": False})
        else:
            # response = render(request, 'login.html', context={"user": {**validated_user_data[0]}})

            # TODO: Check if is possible pass the context through "redirect" function
            response = redirect(reverse('home'), context={"user": {**validated_user_data[0]}})

            # TODO: Build handle session logic
            request.session['user'] = validated_user_data[0]

        return response

    already_user = request.session.get('user')

    if already_user == None:
        response = render(request, 'login.html')
        return response
    
    response = redirect(reverse('home'))
    return response