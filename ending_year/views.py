# ending_year/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

def about_us_view(request):
    return render(request, 'about_us.html')
