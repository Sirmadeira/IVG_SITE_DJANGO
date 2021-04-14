from django.urls import path
from .import views

urlpatterns = [
    path('', views.InsiraDado, name = 'data-InsiraDado'),
    path('VisualMerc/', views.VisualizarMercado, name = 'data-VisualizarMercado'),
    path('Update/<int:id>', views.Update, name = 'data-Update'),
    path('Editar/<int:id>', views.Editar, name = 'data-Editar'),
    path('Deletar/<int:id>', views.Destroir, name = 'data-Deletar'),
]