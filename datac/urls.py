from django.urls import path
from .import views

urlpatterns = [
    path('', views.InsiraDadoC, name = 'datac-InsiraDadoC'),
    ]