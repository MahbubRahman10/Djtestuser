from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

from django.contrib.auth import views as auth_views 

urlpatterns = [
	path('', views.index, name='Home-Page'),
	path('register', views.register, name='Register-Page'),
	path('login', views.login, name='Login-Page'),
	path('logout', views.logout, name='Logout-Page'),
]
