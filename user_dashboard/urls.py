from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render
from . import views

urlpatterns = [
     path("login", views.authLogin, name="login"),
     path("logout", views.authLogout, name="logout"),
]
