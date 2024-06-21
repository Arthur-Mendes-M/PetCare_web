from django.urls import path
from . import views

urlpatterns = [
    path('', views.sales, name='sales'),
    path('/create_sale', views.create_sale, name='create_sale')
]
