from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Correct import from your app's models
from Login.models import Account

from django.contrib.auth.decorators import login_required
from decimal import *


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        # Create a new user with the provided username, email, and password
        User.objects.create_user(username=username, email=email, password=password)
        return redirect("login")
    return render(request, "register.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page or any other page after login
        else:
            error_message = "Invalid credentials. Please try again."
            return render(request, "login.html", {"error_message": error_message})
    return render(request, "login.html")


@login_required
def home(request):
    context = {'username': request.user.username}
    return render(request, "home.html", context)

    

def logout_user(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout






def create_account(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        account_number = request.POST.get('account_number')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        
        new_account = Account(
            name=name,
            account_number=account_number,
            phone_number=phone_number,
            balance=0.00,
        )
        new_account.set_password(password)  # Hash the password
        new_account.save()
        
        return redirect('home')  # Redirect to a success page or home
    return render(request, 'new.html')

def create_account(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        account_number = request.POST.get('account_number')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')

        new_account = Account(
            name=name,
            account_number=account_number,
            phone_number=phone_number,
            balance=0.00,
        )
        new_account.set_password(password)  # Properly hash the password
        new_account.save()

        return redirect('home')
    return render(request, 'new.html')

from decimal import Decimal
from Login.models import Account

def deposit_money(request):
    balance=None
    if request.method == 'POST':
        account_number = request.POST.get('account_number')
        password = request.POST.get('password')
        amount = request.POST.get('amount')

        try:
            account_number = int(account_number)
            amount = Decimal(amount)
        except (ValueError, InvalidOperation):
            return render(request, 'deposit.html', {'error_message': 'Invalid input'})

        try:
            account = Account.objects.get(account_number=account_number)
            if account.check_password(password):
                account.balance += amount
                account.save()
                return render(request, 'deposit.html', {
                    'balance': account.balance,
                    'success_message': 'Deposit successful'
                })
            else:
                return render(request, 'deposit.html', {'error_message': 'Invalid password'})
        except Account.DoesNotExist:
            return render(request, 'deposit.html', {'error_message': 'Account does not exist'})
    
    return render(request, 'deposit.html', {'username': request.user.username, 'balance': balance})

@login_required
def withdraw_money(request):
    balance = None
    if request.method == 'POST':
        account_number = request.POST.get('account_number')
        password = request.POST.get('password')
        amount = request.POST.get('amount')

        try:
            account_number = int(account_number)
            amount = Decimal(amount)
        except (ValueError, InvalidOperation):
            return render(request, 'withdraw.html', {'error_message': 'Invalid input'})

        try:
            account = Account.objects.get(account_number=account_number)
            if account.check_password(password):
                if account.balance >= amount:
                    account.balance -= amount
                    account.save()
                    return render(request, 'withdraw.html', {
                        'balance': account.balance,
                        'success_message': 'Withdrawal successful'
                    })
                else:
                    return render(request, 'withdraw.html', {'error_message': 'Insufficient funds'})
            else:
                return render(request, 'withdraw.html', {'error_message': 'Invalid password'})
        except Account.DoesNotExist:
            return render(request, 'withdraw.html', {'error_message': 'Account does not exist'})
    
    return render(request, 'withdraw.html', {'username': request.user.username, 'balance': balance})



def check_balance(request):
    balance = None
    if request.method == 'POST':
        print("POST request received for check balance")

        account_number = request.POST.get('account_number')
        password = request.POST.get('password')

        # Convert account_number to proper type
        try:
            account_number = int(account_number)
            print(f"Account number: {account_number}")
        except ValueError:
            print("Invalid account number")
            return render(request, 'check_balance.html', {'error_message': 'Invalid account number'})

        # Fetch account and check password
        try:
            account = Account.objects.get(account_number=account_number)
            if account.check_password(password):
                balance = account.balance  # Get balance
                print(f"Balance for account {account_number}: {balance}")
            else:
                print("Invalid password")
                return render(request, 'check_balance.html', {'error_message': 'Invalid password'})
        except Account.DoesNotExist:
            print("Account does not exist")
            return render(request, 'check_balance.html', {'error_message': 'Account does not exist'})
    
    return render(request, 'check_balance.html', {'balance': balance})

def transfer_money(request):
    if request.method == 'POST':
        source_account_number = request.POST.get('source_account_number')
        destination_account_number = request.POST.get('destination_account_number')
        password = request.POST.get('password')
        amount = request.POST.get('amount')

        try:
            source_account_number = int(source_account_number)
            destination_account_number = int(destination_account_number)
            amount = Decimal(amount)
        except (ValueError, InvalidOperation):
            return render(request, 'transfer.html', {'error_message': 'Invalid input'})

        try:
            source_account = Account.objects.get(account_number=source_account_number)
            destination_account = Account.objects.get(account_number=destination_account_number)
            if source_account.check_password(password):
                if source_account.balance >= amount:
                    source_account.balance -= amount
                    destination_account.balance += amount
                    source_account.save()
                    destination_account.save()
                    return render(request, 'transfer.html', {
                        'balance': source_account.balance,
                        'success_message': 'Transfer successful'
                    })
                else:
                    return render(request, 'transfer.html', {'error_message': 'Insufficient funds'})
            else:
                return render(request, 'transfer.html', {'error_message': 'Invalid password'})
        except Account.DoesNotExist:
            return render(request, 'transfer.html', {'error_message': 'One or both accounts do not exist'})
    
    return render(request, 'transfer.html')


@login_required
def change_pin(request):
    if request.method == 'POST':
        account_number = request.POST.get('account_number')
        old_pin = request.POST.get('old_pin')
        new_pin = request.POST.get('new_pin')

        try:
            account_number = int(account_number)
        except ValueError:
            return render(request, 'changepin.html', {'error_message': 'Invalid account number'})

        try:
            account = Account.objects.get(account_number=account_number)
            if account.check_password(old_pin):  # Assuming PIN is stored like a password
                account.set_password(new_pin)  # Hash and set the new PIN
                account.save()
                return render(request, 'changepin.html', {'success_message': 'PIN changed successfully'})
            else:
                return render(request, 'changepin.html', {'error_message': 'Incorrect old PIN'})
        except Account.DoesNotExist:
            return render(request, 'changepin.html', {'error_message': 'Account does not exist'})
    
    return render(request, 'changepin.html')
