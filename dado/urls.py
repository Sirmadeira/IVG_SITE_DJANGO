from django.urls import path
from .import views

urlpatterns = [
path('', views.InserirDado, name = 'dado-InserirDado')]