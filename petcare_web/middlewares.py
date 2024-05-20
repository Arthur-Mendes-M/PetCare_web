from django.shortcuts import redirect
from django.urls import reverse
from access.utils import session_handler
from django.http import HttpResponse
class AuthenticateRoutes:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_employee = session_handler(request, 'employee', False, 'get')

        if not current_employee and not request.path == reverse('login') and not request.path == reverse('signup'):
            print('------not current_employee and not ...-------')
            return redirect(reverse('login'))
        elif current_employee and (request.path == reverse('login') or request.path == reverse('signup')):
            # if the content isn't passed for response, keep the same page (just return success code - 204)
            return HttpResponse(status=204)

        response = self.get_response(request)
        return response
