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
@usuarios_permitidos(allowed_roles=['admin'])
def AutocompleteModelo(request):
	term = request.GET.get('term')
	if term:
		modelos = list(DataDBC.objects.filter(modelo__istartswith=request.GET.get('term')).values_list('modelo', flat=True).order_by("modelo").distinct())
		return JsonResponse(modelos, safe=False)
	return render(request,'data.insiradado.html')

@login_required
@usuarios_permitidos(allowed_roles=['admin'])
def AutocompleteMotor(request):
	term = request.GET.get('term')
	if term:
		motores = list(DataDBC.objects.filter(motor__istartswith=request.GET.get('term')).values_list('motor', flat=True).order_by("motor").distinct())
		return JsonResponse(motores, safe=False)
	return render(request,'data.insiradado.html')

