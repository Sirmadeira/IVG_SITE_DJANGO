from django.shortcuts import render, redirect
from django.db.models import Avg, Count
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import InsiraDadosForm
from .models import DataDB
from .decorators import usuarios_permitidos
from .utils import get_plot
from rest_framework.views import APIView
from rest_framework.response import Response


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
	#Query para tabela crud!
	query1= DataDB.objects.filter(autor = user ).all()
	#Query para tabela top 10 marcas mais vendidas
	query2= DataDB.objects.values('marca').annotate(marcas=Count('marca')).order_by('-marcas')
	#Query para tabela top 10 modelos mais vendidos
	query3= DataDB.objects.values('marca','modelo','motor','ano').annotate(modelos=Count('modelo')).order_by('-modelos')
	#Query para tabela de media de lucro mais vendidos
	query4=DataDB.objects.values('marca','modelo','motor','ano').annotate(medias=Avg('margem_de_lucro')).order_by('-medias')
	#Plots
	query5= DataDB.objects.only('marca','preco')
	x = [x.marca for x in query5]
	y = [y.preco for y in query5]
	grafico1= get_plot(x,y)
	if contador < 5 :
		return render(request, 'data/semdados.html', {'contador' : contador, 'faltante' : faltante})
	return render(request, 'data/visualizarmercado.html', {'query1': query1,'query2':query2,'query3':query3,'query4':query4,'grafico1':grafico1})

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
@usuarios_permitidos(allowed_roles=['admin'])
def AutocompleteModelo(request):
	term = request.GET.get('term')
	if term:
		modelos = list(DataDB.objects.filter(modelo__istartswith=request.GET.get('term')).values_list('modelo', flat=True).order_by("modelo").distinct())
		return JsonResponse(modelos, safe=False)
	return render(request,'data.insiradado.html')

@login_required
@usuarios_permitidos(allowed_roles=['admin'])
def AutocompleteMotor(request):
	term = request.GET.get('term')
	if term:
		motores = list(DataDB.objects.filter(motor__istartswith=request.GET.get('term')).values_list('motor', flat=True).order_by("motor").distinct())
		return JsonResponse(motores, safe=False)
	return render(request,'data.insiradado.html')

class DadosDeGrafico(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
    	data = list(DataDB.objects.values('marca').all())
    	return Response(data)