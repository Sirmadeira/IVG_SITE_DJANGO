from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.conf import settings

User= settings.AUTH_USER_MODEL

class CustomUser(AbstractUser):
	SEXO_CHOICES = (
        ("R", "Revendedora"),
        ("C", "Concessionária"),
    )
	setor= models.CharField(max_length=1,choices=SEXO_CHOICES, blank=False, null=False)

class EmpresaDB(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to= 'empresa_pics')

	def __str__(self):
		return f'{self.user.username} Empresa'

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)

# Create your models here.
