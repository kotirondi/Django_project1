"""
URL configuration for BankManagementSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

"""from django.urls import path
from django.conf.urls.static import static
from django.conf import  settings
from .views import login_user,register,logout_user

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",login_user,name="login"),
    path("register/",register,name="register"),
]
"""
from django.urls import path
from .views import user_login, register, logout_user,home, create_account,deposit_money,withdraw_money,check_balance,transfer_money,change_pin

urlpatterns = [
    path('', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('admin/', admin.site.urls),
    path('home/', home, name="home"),
    path('new_account/', create_account, name='new_account'),
    path('new/', create_account, name='account'),

    path('deposit/', deposit_money, name='deposit'),
      path('withdraw/', withdraw_money, name='withdraw'),
      path('check_balance/', check_balance, name='check_balance'),
      path('transfer/', transfer_money, name='transfer'),
    
    # Other URL patterns
    path('change_pin/', change_pin, name='change_pin'),

]
