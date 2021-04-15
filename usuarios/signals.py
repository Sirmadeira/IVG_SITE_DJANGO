from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from .models import EmpresaDB

User= settings.AUTH_USER_MODEL

@receiver(post_save, sender= User)
def create_empresa(sender, instance, created, **kwargs):
	if created:
		EmpresaDB.objects.create(user=instance)

@receiver(post_save, sender= User)
def save_empresa(sender, instance,**kwargs):
	instance.empresadb.save()





