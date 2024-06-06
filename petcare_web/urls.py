from django.urls import path, include

urlpatterns = [
    path('', include('access.urls')),
    path('home', include('home.urls'), name='home'),
    path('analytics', include('analytics.urls'), name='analytics'),
    path('sales', include('sales.urls'), name='sales'),

    path('reports', include('reports.urls'), name='reports'),
    path('user_profile', include('user_profile.urls'), name='user_profile')
]