from django.contrib import admin
from django.urls import path, include
from .views import login, register,signout,perfil
urlpatterns = [
    path('', login, name="login"),
    path('login', login, name="login"),
    path('register', register, name="register"),
    path('perfil', perfil, name="perfil"),
    path('signout', signout, name="signout")
]