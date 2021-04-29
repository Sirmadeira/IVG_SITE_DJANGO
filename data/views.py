from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import InsiraDadosForm
from .models import DataDB
from .decorators import usuarios_permitidos


@login_required
@usuarios_permitidos(allowed_roles=['admin','cliente_checado'])
def InsiraDado(request):
	if request.method == 'POST':
		form = InsiraDadosForm(request.POST)
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
			lucro=form.cleaned_data.get('lucro')
			form.instance.margem_de_lucro = (lucro/preco)*100
			form.save()
			messages.success(request, f'Seus dados foram inseridos com sucesso!')
			return redirect('data-InsiraDado')
	else:
		form = InsiraDadosForm()
	return render(request, 'data/insiradado.html', {'form': form})
	
@login_required
@usuarios_permitidos(allowed_roles=['admin','cliente_checado'])
def VisualizarMercado(request):
	user= request.user
	contador = DataDB.objects.filter(autor = user).count()
	faltante = 5-contador
	if contador < 5 :
		return render(request, 'data/semdados.html', {'contador' : contador, 'faltante' : faltante})
	query= DataDB.objects.all()
	return render(request, 'data/visualizarmercado.html', {'query': query})

@login_required
@usuarios_permitidos(allowed_roles=['admin','cliente_checado'])
def Update(request, pk):
	dado = DataDB.objects.get(id=pk)
	form = InsiraDadosForm(instance=dado)
	if request.method == 'POST':
		form = InsiraDadosForm(request.POST, instance=dado)
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
			lucro=form.cleaned_data.get('lucro')
			form.instance.margem_de_lucro = (lucro/preco)*100
			form.save()
			messages.success(request, f'Seus dados foram atualizados com sucesso!')
			return redirect('data-VisualizarMercado')
	return render(request, 'data/insiradado.html', {'form':form})

@login_required
@usuarios_permitidos(allowed_roles=['admin','cliente_checado'])
def Destroir(request, pk):  
    query = DataDB.objects.get(id=pk)  
    query.delete()  
    return redirect("data-VisualizarMercado")  

@login_required
def AutocompleteModelo(request):
	term = request.GET.get('term')
	if term:
		modelos = list(DataDB.objects.filter(modelo__istartswith=request.GET.get('term')).values_list('modelo', flat=True).order_by("modelo").distinct())
		return JsonResponse(modelos, safe=False)
	return render(request,'data.insiradado.html')

@login_required
def AutocompleteMotor(request):
	term = request.GET.get('term')
	if term:
		motores = list(DataDB.objects.filter(motor__istartswith=request.GET.get('term')).values_list('motor', flat=True).order_by("motor").distinct())
		return JsonResponse(motores, safe=False)
	return render(request,'data.insiradado.html')
