from django import forms
from django.forms import ModelForm
from .models import DadoDB


class InsiraDadosForm(ModelForm):
	class Meta:
		model = DadoDB
		fields = ['marca','modelo','ano','status','cor','combustivel','quilometragem','lucro','preco','margem_de_lucro']