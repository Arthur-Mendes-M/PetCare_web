from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('/create_product', views.create_product, name='create_product'),
    path('/edit_product', views.edit_product, name='edit_product'),
    path('/delete_product', views.delete_product, name='delete_product'),
]