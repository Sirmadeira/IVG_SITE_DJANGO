from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings

User= settings.AUTH_USER_MODEL

class DataDBC(models.Model):
	localidade_escolhas = (
        ("P", "Piracicaba"),
        ("L", "Limeira"),
    )
	status_escolhas = (
        ("E", "Excelente"),
        ("B", "Bom"),
        ("M", "Mediano"),
        ("R", "Ruim"),
        ("T", "Terrível"),
    )
	combustivel_escolhas = (
        ("G", "Gasolina"),
        ("E", "Etanol"),
        ("G", "GNV"),
        ("D", "Diesel"),
        ("F", "Flex"),
    )
	
	marca=models.CharField(max_length = 30,error_messages={'required':'Favor inserir uma marca'})

	modelo=models.CharField(max_length = 60,error_messages={'required':'Favor inserir um modelo'})

	motor=models.CharField(max_length = 60,error_messages={'required':'Favor inserir um motor'})

	ano=models.IntegerField(
		validators=[MinValueValidator(1960,'Favor inserir acima 1960.'), MaxValueValidator(2023,'Favor inserir abaixo 2023.')],
		error_messages={'required':'Favor inserir uma ano'})

	localidade=models.CharField(choices=localidade_escolhas,max_length = 1,blank=False, null=False)
	
	status=models.CharField(choices=status_escolhas,max_length = 1,blank=False, null=False)

	cor=models.CharField(max_length= 20)

	combustivel=models.CharField(choices=combustivel_escolhas,max_length = 1,blank=False, null=False)

	quilometragem=models.DecimalField(max_digits= 10,decimal_places=2,max_length= 12,
		validators=[MinValueValidator(0,'Não existe quilometragem negativa'),MaxValueValidator(99999999,'Favor inserir valor menor')])

	preco=models.DecimalField(max_digits= 12,decimal_places=2,max_length= 12,
		validators=[MinValueValidator(1000.00,'Favor inserir vendas acima de 1000 reais'),MaxValueValidator(99999999,'Favor inserir valor menor')])

	data_postada = models.DateTimeField(default=timezone.now)

	autor = models.ForeignKey(User, on_delete=models.CASCADE)
