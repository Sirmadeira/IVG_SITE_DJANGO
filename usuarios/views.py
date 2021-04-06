from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def Cadastro(request):
	form = UserCreationForm()
	return render(request, 'usuarios/Cadastro.html', {'form': form})
