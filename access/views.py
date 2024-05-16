from django.shortcuts import render, redirect

# Create your views here.

def login(request):
    if request.method == 'POST':
        # verify is user exists
        pass

    already_user = request.COOKIES.get('user')

    if already_user:
        return redirect('home')
    
    return render(request, 'login.html')