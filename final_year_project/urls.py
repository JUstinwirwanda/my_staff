# final_year_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ending_year.urls')),  # Add this line for the root path
    # Add other URL patterns as needed
]

