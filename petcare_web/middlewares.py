from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import get_template

from utils.session_handler import session_handler
class AuthenticateRoutes:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_employee = session_handler(request, 'employee', False, 'get')
        response = self.get_response(request)

        if not current_employee and not request.path == reverse('login') and not request.path == reverse('signup'):
            return redirect(reverse('login'))
        elif current_employee and (request.path == reverse('login') or request.path == reverse('signup')):
            # if the content isn't passed for response, keep the same page (just return success code - 204)
            return HttpResponse(status=204)
        
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
