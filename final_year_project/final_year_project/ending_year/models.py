# ending_year/models.py
from django.db import models

class Citizen(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.second_name}"

class JuniorLeader(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    national_identity = models.CharField(max_length=20)
    nationality = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    marital_status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.second_name}"
