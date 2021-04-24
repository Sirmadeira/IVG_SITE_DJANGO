from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import CustomUser,EmpresaDB


#Mecanicas chatas para alterar validators labels etc de criacao de usuario

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Usuário',widget=forms.TextInput())
    password = forms.CharField(label='Senha',widget=forms.PasswordInput())
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.error_messages['invalid_login'] = 'Usuário ou senha inválido'
        super().__init__(*args, **kwargs)


class UserCadastroForm(UserCreationForm):
	error_messages = {
        'password_mismatch': "Essas senhas não são iguais",
    }
	class Meta:
		model = CustomUser
		fields = ['username', 'email','setor','password1', 'password2' ]
		labels={'username':'Usuário','setor':'Setor da sua empresa'}
		error_messages= {
			'username': {
			'unique': 'Esse usuário já existe'
			},
			'email':{
			'unique':'Esse email já está cadastrado'
			}
		}
		help_texts={'username':'Favor evitar uso de carateres especiais, algo além desses @/./+/-/_ não será aceito'}
	# Chatice para alterar label de senha
	def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.fields['password1'].label = 'Senha'
          self.fields['password2'].label = 'Confirmar senha'
          self.fields['password1'].help_text='''* Sua senha precisa ter 8 caracteres
												* Sua senha não pode ser muito comum
												* Sua senha não pode ser só números'''
          self.fields['password2'].help_text='Favor por a mesma senha neste campo'

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