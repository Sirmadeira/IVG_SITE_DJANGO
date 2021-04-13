from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import InsiraDadosForm
from .models import DataDB

# Views crud

@login_required
def InsiraDado(request):
	if request.method == 'POST':
		form = InsiraDadosForm(request.POST)
		if form.is_valid():
			form.instance.autor = request.user
			form.save()
			print(request.POST)
			messages.success(request, f'Seus dados foram inseridos com sucesso!')
			return redirect('data-InsiraDado')
	else:
		form = InsiraDadosForm()
	return render(request, 'data/insiradado.html', {'form': form})

def edit(request, id):
    query = DataDB.objects.get(id=id)
    return render(request, 'edit.html', {'query': query})

def update(request, id):
    query = DataDB.objects.get(id=id)  
    form = InsiraDadoForms(request.POST, instance = datadb)  
    if form.is_valid():  
        form.save()  
        return redirect("/")
    return render(request, 'edit.html', {'query': query})

def delete(request, id):
    query = DataDB.objects.get(id=id)
    query.delete()
    return redirect('/')

def VisualizarMercado(request):
	query = DataDB.objects.all()
	return render(request, 'data/visualizarmercado.html', {'query': query})
