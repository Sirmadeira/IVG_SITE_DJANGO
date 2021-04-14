from django.urls import path
from .import views

urlpatterns = [
    path('', views.InsiraDado, name = 'data-InsiraDado'),
    path('VisualMerc/', views.VisualizarMercado, name = 'data-VisualizarMercado'),
]