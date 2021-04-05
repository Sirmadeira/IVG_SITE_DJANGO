from django.shortcuts import render


def Homepage(request):
	return render(request, 'APP_IVG/homepage.html')

def Sobre(request):
	return render(request,'APP_IVG/sobre.html', {'titulo': 'Sobre'})

# Create your views here.
