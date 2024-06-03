from django.shortcuts import render, redirect
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
            response = render(request, 'login.html', {'login_error': 'E-mail e/ou senha incorreto(s)'})
            
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
    
        response = Employees().save_one(data=data, files=file)
        response_in_str = str(response.json())

        if response.status_code == 200:
            return redirect(reverse('login'))
        
        signup_error = "Ocorreu algum erro no cadastro :/ Pedimos que, por favor, reinicie a página e tente novamente."

        if 'already exists' in response_in_str:
            signup_error = "Esse e-mail já existe! Utilize outro."
        elif 'megabyte' in response_in_str:
            signup_error = "Imagem muito grande ou no formato incorreto. Utilize imagens de até 3M e com extensões .jpeg, .jpg ou .png"

        return render(request, 'signup.html', {"signup_error": signup_error})


    return render(request, 'signup.html')

def logout(request):
    session_handler(request, 'employee', None, 'delete')

    return redirect(reverse('login'))