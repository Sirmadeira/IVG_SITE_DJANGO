from django.urls import path
from .import views

urlpatterns = [
    path('', views.InsiraDado, name = 'data-InsiraDado'),
    path('VisualMerc/', views.VisualizarMercado, name = 'data-VisualizarMercado'),
    path('Update/<str:pk>', views.Update, name = 'data-Update'),
    path('Deletar/<str:pk>', views.Destroir, name = 'data-Deletar'),
    path('AutocompModelo', views.AutocompleteModelo, name = 'data-AutocompleteModelo'),
    path('AutocompMotor', views.AutocompleteMotor, name = 'data-AutocompleteMotor'),
    path('DadosDeModeloIns', views.DadosDeModeloIns, name= 'data-DadosDeModeloIns'),
    path('DadosDeMotorIns', views.DadosDeMotorIns, name= 'data-DadosDeMotorIns'),
]