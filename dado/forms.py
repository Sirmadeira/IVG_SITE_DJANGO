from django import forms
from .models import DadoDB


class InsiraDadosForm(forms.ModelForm):
	class Meta:
		model = DadoDB
		fields = ['marca','modelo','ano','status','cor','combustivel','quilometragem','lucro','preco','margem_de_lucro']