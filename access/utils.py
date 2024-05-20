import json
import requests
import os

def validate_access(email, password):
    petcare_validate_employee_url = f"{os.getenv('PETCARE_API_URL')}employees/?auth={os.getenv('PETCARE_AUTH_TOKEN')}"
    petcare_validate_headers = {
        'Content-Type': 'application/json'
    }
    petcare_validate_content_data = json.dumps({
        'email': email,
        'password': password
    })

    response = requests.get(petcare_validate_employee_url, headers=petcare_validate_headers, data=petcare_validate_content_data)
    response_in_json = response.json()

    if response.status_code == 400:
        return {
            'employee': False,
            'response': response
        }

    return {
        'employee': response_in_json[0],
        'response': response
    }

def session_handler(request, variable_name, variable_value='', action='get'):    
    data_to_return = ''
    action = action.lower()

    match action:
        case 'get':
            data_to_return = request.session.get(variable_name)
        case 'set':
            request.session[variable_name] = variable_value
            data_to_return = True
        case 'update':
            if variable_name in request.session:
                del request.session[variable_name]
                request.session[variable_name] = variable_value
                data_to_return = True
            else:
                data_to_return = False
        case 'delete':
            if variable_name in request.session:
                del request.session[variable_name]
                data_to_return = True
            else:
                data_to_return = False

    return data_to_return
