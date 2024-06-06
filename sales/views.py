from django.shortcuts import render

def sales(request):
    return render(request, 'sales/index.html')