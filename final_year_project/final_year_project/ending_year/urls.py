# ending_year/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Add other URL patterns as needed
]
