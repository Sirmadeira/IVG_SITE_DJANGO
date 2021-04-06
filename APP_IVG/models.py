from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Dados(models.Model):
	data_postada = models.DateTimeField(default=timezone.now)
	autor= models.ForeignKey(User, on_delete=models.CASCADE)
