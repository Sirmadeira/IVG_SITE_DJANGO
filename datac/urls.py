from django.urls import path
from .import views

urlpatterns = [
    path('', views.InsiraDadoC, name = 'datac-InsiraDadoC'),
    path('Update/<str:pk>', views.Update, name = 'datac-Update'),
    path('Deletar/<str:pk>', views.Destroir, name = 'datac-Deletar'),
    ]