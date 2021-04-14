from django import forms
from .models import DataDB


class InsiraDadosForm(forms.ModelForm):
	class Meta:
		model = DataDB
		fields = ['marca','modelo','ano','status','cor','combustivel','quilometragem','lucro','preco','margem_de_lucro']
