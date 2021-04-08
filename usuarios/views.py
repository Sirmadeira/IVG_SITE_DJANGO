from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserCadastroForm



def Cadastro(request):
	if request.method == 'POST':
		form = UserCadastroForm(request.POST)
		if form.is_valid():
			form.save()
			username= form.cleaned_data.get('username')
			messages.success(request, f'Sua conta foi criada com sucesso!')
			return redirect('Login')
	else:
		form = UserCadastroForm()
	return render(request, 'usuarios/cadastro.html', {'form': form})

@login_required
def Empresa(request):
	return render(request,	'usuarios/empresa.html')
