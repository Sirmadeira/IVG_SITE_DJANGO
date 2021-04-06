from django.shortcuts import render
from .models import Dado 

def Homepage(request):
	return render(request, 'APP_IVG/homepage.html')

def Sobre(request):
	return render(request,'APP_IVG/sobre.html', {'titulo': 'Sobre'})

def Faq(request):
	return render(request, 'APP_IVG/faq.html', {'titulo': 'Faq'})

# Create your views here.
