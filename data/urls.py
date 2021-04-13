from django.urls import path
from .import views

urlpatterns = [
 path('', views.InsiraDado, name = 'data-InsiraDado'),
 path('VisualMerc/', views.VisualizarMercado, name = 'data-VisualizarMercado'),
 path('edit/<int:id>', views.edit),  
 path('update/<int:id>', views.update),  
 path('delete/<int:id>', views.delete),
]