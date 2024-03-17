from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm

from django.contrib.auth.models import auth

from django.contrib import messages

from .models import User




# Create your views here.

def index(request):
	return render(request, "index.html")

def register(request):
	if request.user.is_authenticated:
		return redirect("Home-Page")
	else:
		if request.method == "POST":
			form = UserForm(request.POST)
			if form.is_valid():
				user = form.save()
				messages.success(request, f'Please confirm your email address to complete the registration')

				return redirect('Register-Page')

		else:
			form = UserForm()
			return render(request, "register.html", {'form':form})

		return render(request, "register.html", {'form':form})


def login(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']

		user = auth.authenticate(email = email, password = password)

		if user is not None:
			auth.login(request, user)
			if 'remember' in request.POST:
				request.session.set_expiry(0)
			return redirect('Home-Page')
		else:
			messages.warning(request, f'Invalid credentials')
			return redirect('Login-Page')
	else:
		return render(request,"login.html")

def logout(request):
	auth.logout(request)
	return redirect("Home-Page")
