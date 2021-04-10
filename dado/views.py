from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import InsiraDadosForm


@login_required
def InserirDado(request):
	if request.method == 'POST':
		form = InsiraDadosForm(request.POST,instance= request.user)
		if form.is_valid():
			form.save()
			print(request.POST)
			messages.success(request, f'Seus dados foram inseridos com sucesso!')
			return redirect('dado-InserirDado')
	else:
		form = InsiraDadosForm()
	return render(request, 'dado/inserirdado.html', {'form': form})

# Create your views here.
