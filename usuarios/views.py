from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserCadastroForm
def Cadastro(request):
	if request.method == 'POST':
		form = UserCadastroForm(request.POST)
		if form.is_valid():
			form.save()
			username= form.cleaned_data.get('username')
			messages.success(request, f'Conta criada para {username}!')
			return redirect('APP_IVG-Homepage')
	else:
		form = UserCadastroForm()
	return render(request, 'usuarios/Cadastro.html', {'form': form})
