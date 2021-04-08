from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import EmpresaDB

class UserCadastroForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2' ]

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']

class EmpresaUpdateForm(forms.ModelForm):
	class Meta:
		model = EmpresaDB
		fields = ['image']	