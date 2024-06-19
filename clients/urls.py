from django.urls import path
from . import views

urlpatterns = [
    path('', views.clients, name='clients'),
    path('/create_client', views.create_client, name='create_client'),
    path('/edit_client', views.edit_client, name='edit_client'),
    path('/delete_client', views.delete_client, name='delete_client'),
]