# your_app/admin.py

from django.contrib import admin
from .models import Useradd, Account

@admin.register(Useradd)
class UseraddAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'name', 'aadhar_number', 'balance', 'date_of_creation')
