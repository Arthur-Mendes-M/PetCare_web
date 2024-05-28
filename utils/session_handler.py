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