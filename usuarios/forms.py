from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCadastroForm(UserCreationForm):
	email = forms.EmailField()

	class meta:
		model = User
		fields = ['Usuario', 'Email', 'Password1', 'Password2' ]