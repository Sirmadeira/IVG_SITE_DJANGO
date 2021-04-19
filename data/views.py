from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import InsiraDadosForm
from .models import DataDB


@login_required
def InsiraDado(request):
	if request.method == 'POST':
		form = InsiraDadosForm(request.POST)
		if form.is_valid():
			submitbutton= request.POST.get("submit")
			form.instance.autor = request.user
			preco=form.cleaned_data.get('preco')
			lucro=form.cleaned_data.get('lucro')
			form.instance.margem_de_lucro = (lucro/preco)*100
			form.save()
			print(request.POST)
			messages.success(request, f'Seus dados foram inseridos com sucesso!')
			return redirect('data-InsiraDado')
	else:
		form = InsiraDadosForm()
	return render(request, 'data/insiradado.html', {'form': form})
	
@login_required
def VisualizarMercado(request):
	query= DataDB.objects.all()
	return render(request, 'data/visualizarmercado.html', {'query': query})

@login_required
def Destroir(request, id):  
    query = DataDB.objects.get(id=id)  
    query.delete()  
    return redirect("data-VisualizarMercado") 