from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name="home"),
    path('register' , register_attempt , name="register_attempt"),
    path('authapp/login/' , login_attempt , name="login_attempt"),
    path('token' , token_send , name="token_send"),
    path('success' , success , name='success'),
    path('verify/<auth_tokens>' , verify , name="verify"),
    path('error' , error_page , name="error")
   
]