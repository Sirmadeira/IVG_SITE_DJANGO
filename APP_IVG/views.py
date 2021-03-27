from django.shortcuts import render
from django.http import HttpResponse


def Homepage(request):
	return HttpResponse('<h1> IVG HOME </h1>')

def Sobre(request):
	return HttpResponse('<h1> IVG SOBRE </h1>')

# Create your views here.
