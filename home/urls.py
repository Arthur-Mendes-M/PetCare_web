from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/create_employee', views.create_employee, name='create_employee'),
    path('/edit_employee', views.edit_employee, name='edit_employee'),
    path('/delete_employee', views.delete_employee, name='delete_employee'),
]