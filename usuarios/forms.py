from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,EmpresaDB



class UserCadastroForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = CustomUser
		fields = ['username', 'email', 'password1','setor', 'password2' ]
		labels={'username':'Usuário','setor':'Setor da sua empresa','password1':'Senha','password2':'Confirmar senha'}

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = CustomUser
		fields = ['username', 'email']
		labels = {'username':'Usuário'}

class EmpresaUpdateForm(forms.ModelForm):
	class Meta:
		model = EmpresaDB
		fields = ['image']
		labels={'image': 'Logo da sua empresa'}	