from django.shortcuts import render
from django.shortcuts import render, redirect
from django.db.models import Avg, Count
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import InsiraDadosFormC
from .models import DataDBC
from data.decorators import usuarios_permitidos

@login_required
@usuarios_permitidos(allowed_roles=['admin','cliente_checado'])
def InsiraDadoC(request):
	if request.method == 'POST':
		form = InsiraDadosFormC(request.POST)
		if form.is_valid():
			submitbutton= request.POST.get("submit")
			form.instance.autor = request.user
			#Transforma a data de marca modelo e cor em maiusculo
			marca= form.cleaned_data.get('marca').upper()
			modelo=form.cleaned_data.get('modelo').upper()
			motor=form.cleaned_data.get('motor').upper()
			cor=form.cleaned_data.get('cor').upper()
			form.instance.marca= marca
			form.instance.modelo= modelo
			form.instance.motor= motor
			form.instance.cor= cor
			form.save()
			messages.success(request, f'Seus dados foram inseridos com sucesso!')
			return redirect('data-InsiraDado')
	else:
		form = InsiraDadosFormC()
	return render(request, 'datac/insiradadocompras.html', {'form': form})

@login_required
@usuarios_permitidos(allowed_roles=['admin','cliente_checado'])
def Update(request, pk):
	dado = DataDBC.objects.get(id=pk)
	form = InsiraDadosFormC(instance=dado)
	if request.method == 'POST':
		form = InsiraDadosFormC(request.POST, instance=dado)
		if form.is_valid():
			submitbutton= request.POST.get("submit")
			form.instance.autor = request.user
			#Transforma a data de marca modelo e cor em maiusculo
			marca= form.cleaned_data.get('marca').upper()
			modelo=form.cleaned_data.get('modelo').upper()
			motor=form.cleaned_data.get('motor').upper()
			cor=form.cleaned_data.get('cor').upper()
			form.instance.marca= marca
			form.instance.modelo= modelo
			form.instance.motor= motor
			form.instance.cor= cor
			# Formula a margem de lucro
			preco=form.cleaned_data.get('preco')
			form.save()
			messages.success(request, f'Seus dados foram atualizados com sucesso!')
			return redirect('data-VisualizarMercado')
	return render(request, 'datac/insiradadocompras.html', {'form':form})

@login_required
@usuarios_permitidos(allowed_roles=['admin','cliente_checado'])
def Destroir(request, pk):  
    query = DataDBC.objects.get(id=pk)  
    query.delete()  
    return redirect("data-VisualizarMercado")

