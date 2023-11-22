# ending_year/admin.py
from django.contrib import admin
from .models import Citizen, JuniorLeader

admin.site.register(Citizen)
admin.site.register(JuniorLeader)
