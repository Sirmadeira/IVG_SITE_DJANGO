from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,EmpresaDB



class UserCadastroForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = CustomUser
		fields = ['username', 'email','setor','password1', 'password2' ]
		labels={'username':'Usuário','setor':'Setor da sua empresa'}
	# Chatice para alterar label de senha
	def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.fields['password1'].label = 'Senha'
          self.fields['password2'].label = 'Confirmar senha'

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