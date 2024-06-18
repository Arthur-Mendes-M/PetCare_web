from django.urls import path, include

urlpatterns = [
    path('', include('access.urls')),
    path('home', include('home.urls'), name='home'),
    path('clients', include('clients.urls'), name='clients'),
    path('products', include('products.urls'), name='products'),

    path('sales', include('sales.urls'), name='sales'),
    path('user_profile', include('user_profile.urls'), name='user_profile')
]