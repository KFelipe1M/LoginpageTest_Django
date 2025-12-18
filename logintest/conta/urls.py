from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),
    path('home/', views.home, name='home'),
]