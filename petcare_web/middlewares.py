from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseNotFound
from django.template.loader import get_template

from utils.session_handler import session_handler
class AuthenticateRoutes:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_employee = session_handler(request, 'employee', False, 'get')
        response = self.get_response(request)

        target_path = request.path

        if not current_employee and target_path != reverse('login') and target_path != reverse('signup'):
            return redirect(reverse('login'))
        if current_employee and target_path == reverse('login'):
            return redirect(reverse('home'))
        
        return response

class ErrorHandler:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response.status_code == 404:
            template = get_template('errors/404.html')

            response = HttpResponseNotFound(template.render({"error": "404, Page not found!!."}))
        
        return response
