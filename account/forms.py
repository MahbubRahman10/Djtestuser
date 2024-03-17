from django import forms
from django.forms import ModelForm

from .models import User

from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):

	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['email', 'password1', 'password2']
		help_texts = {
		'email': None,
		'password1': None,
		'password2': None,
		}


