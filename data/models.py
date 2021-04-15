from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings

User= settings.AUTH_USER_MODEL

class DataDB(models.Model):
	marca=models.CharField(max_length = 30, default ="ACURA")

	modelo=models.CharField(max_length = 30, default="XWZ")

	ano=models.IntegerField(default= 2021)

	status=models.CharField(max_length= 10,default= "BOM")

	cor=models.CharField(max_length= 10, default= "VERMELHO")

	combustivel=models.CharField(max_length= 10,default= "FLEX")

	quilometragem=models.DecimalField(max_digits= 10,decimal_places=2,max_length= 12,default=100)

	lucro=models.DecimalField(max_digits= 10,decimal_places=2,max_length= 12,default=100)

	preco=models.DecimalField(max_digits= 10,decimal_places=2,max_length= 12,default=100)

	margem_de_lucro=models.DecimalField(max_digits= 10,decimal_places=2,max_length= 12,default=100)

	data_postada = models.DateTimeField(default=timezone.now)

	autor = models.ForeignKey(User, on_delete=models.CASCADE, default = 1)

