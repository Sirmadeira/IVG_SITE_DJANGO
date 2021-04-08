from django.db import models
from django.contrib.auth.models import User

class EmpresaDB(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to= 'empresa_pics')

	def __str__(self):
		return f'{self.user.username} Empresa'


# Create your models here.
