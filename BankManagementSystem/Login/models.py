from django.db import models

# Create your models here.
from datetime import datetime

class Useradd(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.username
    

# your_app/models.py

from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Account(models.Model):
    account_number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    aadhar_number = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=255)  # Store hashed passwords
    phone_number = models.CharField(max_length=15)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date_of_creation = models.DateTimeField(auto_now_add=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.name

