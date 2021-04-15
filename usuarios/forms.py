from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,EmpresaDB



class UserCadastroForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = CustomUser
		fields = ['username', 'email', 'password1','setor', 'password2' ]

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = CustomUser
		fields = ['username', 'email']

class EmpresaUpdateForm(forms.ModelForm):
	class Meta:
		model = EmpresaDB
		fields = ['image']	