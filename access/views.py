from django.shortcuts import render, redirect
from django.urls import reverse
from .utils import validate_access
from .utils import session_handler
from django.contrib import messages

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def login(request):
    if request.method == 'POST':
        # verify is user exists
        email = request.POST.get('email')
        password = request.POST.get('password')
       
        validated_user_data = validate_access(email, password)['employee']

        if not validated_user_data:
            messages.error(request, 'E-mail ou senha incorretos!')
            response = render(request, 'login.html')
        else:
            response = redirect(reverse('home'))

            session_handler(request, 'employee', validated_user_data, 'set')
            # request.session['employee'] = validated_user_data

        return response

    # already_user = request.session.get('employee')
    already_user = session_handler(request, 'employee', False, 'get')

    if already_user == None:
        response = render(request, 'login.html')
        return response

    response = redirect(reverse('home'))
    return response