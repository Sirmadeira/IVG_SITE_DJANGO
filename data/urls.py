from django.urls import path
from .import views

urlpatterns = [
    path('', views.InsiraDado, name = 'data-InsiraDado'),
    path('VisualMerc/', views.VisualizarMercado, name = 'data-VisualizarMercado'),
    path('Deletar/<int:id>', views.Destroir, name = 'data-Deletar'),
    path('AutocompModelo', views.AutocompleteModelo, name = 'data-AutocompleteModelo'),
    path('AutocompMotor', views.AutocompleteMotor, name = 'data-AutocompleteMotor'),
]