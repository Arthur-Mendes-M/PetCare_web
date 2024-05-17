from django.shortcuts import render

# TODO: Access context (user information) from context of redirect
# TODO: Check if is possible pass the context through "redirect" function

# TODO: build a middleware to handle with invalid access through the URL

def home(request):
    # print('------request.context-------')
    # print(request.context)
    # print('-------------')
    return render(request, 'index.html')