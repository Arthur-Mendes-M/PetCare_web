from django.shortcuts import redirect
from django.urls import reverse
from access.utils import session_handler

class AuthenticateRoutes:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_employee = session_handler(request, 'employee', False, 'get')

        if not current_employee and not request.path == reverse('login'):
            return redirect(reverse('login'))

        response = self.get_response(request)
        return response
