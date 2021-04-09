from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Dado(models.Model):
	data_postada = models.DateTimeField(default=timezone.now)
	autor= models.ForeignKey(User, on_delete=models.CASCADE)
	
# Create your models here.
