import os
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from .forms import UserCadastroForm, UserUpdateForm, EmpresaUpdateForm


def Cadastro(request):
	if request.method == 'POST':
		form = UserCadastroForm(request.POST)
		if form.is_valid():
			submitbutton= request.POST.get("submit")
			email_subject = 'Ative sua conta!'
			email_body ='batata'
			email_sender = os.environ.get('MAIL_USERNAME')
			email_usuario = form.cleaned_data.get('email')
			email_verif= EmailMessage(
				email_subject,
				email_body,
				email_sender,
				[email_usuario],
				)
			print(email_usuario)
			print(email_sender)
			email_verif.send(fail_silently=False)
			form.save()
			messages.success(request, f'Sua conta foi criada com sucesso!Favor verificar seu email para poder ter acesso!')
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
