from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import CustomUser,EmpresaDB


#Mecanicas chatas para alterar valor natural dos forms

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(label='Usuário',widget=forms.TextInput())
    password = forms.CharField(label='Senha',widget=forms.PasswordInput())

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