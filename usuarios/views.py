from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import UserCadastroForm, UserUpdateForm, EmpresaUpdateForm


def Cadastro(request):
	if request.method == 'POST':
		form = UserCadastroForm(request.POST)
		if form.is_valid():
			user=form.save()
			username=form.cleaned_data.get('username')

			group = Group.objects.get(name='cliente_nao_checado')
			user.groups.add(group)

			messages.success(request, f'Sua conta foi criada com sucesso!Favor aguardar enquanto a gente verifica se você é um parceiro!')
			return redirect('Login')
	else:
		form = UserCadastroForm()
	return render(request, 'usuarios/cadastro.html', {'form': form})

@login_required
def Empresa(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		e_form = EmpresaUpdateForm(request.POST,request.FILES,instance=request.user.empresadb)

		if u_form.is_valid() and e_form.is_valid():
			u_form.save()
			e_form.save()
			messages.success(request, f'As infos da sua empresa foram atualizadas com sucesso!')
			return redirect('Empresa')
	else:
		u_form = UserUpdateForm(instance=request.user)
		e_form = EmpresaUpdateForm(instance=request.user.empresadb)

	contexto = {
		'u_form': u_form,
		'e_form': e_form,
	}
	return render(request,	'usuarios/empresa.html', contexto)
