# ending_year/urls.py
from django.urls import path
from .views import index, login_view, register_view, about_us_view

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('about_us/', about_us_view, name='about_us'),
    # Add other URL patterns as needed
]
