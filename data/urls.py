from django.urls import path
from .import views
from .views import DadosDeGrafico1

urlpatterns = [
    path('', views.InsiraDado, name = 'data-InsiraDado'),
    path('VisualMerc/', views.VisualizarMercado, name = 'data-VisualizarMercado'),
    path('Update/<str:pk>', views.Update, name = 'data-Update'),
    path('Deletar/<str:pk>', views.Destroir, name = 'data-Deletar'),
    path('AutocompModelo', views.AutocompleteModelo, name = 'data-AutocompleteModelo'),
    path('AutocompMotor', views.AutocompleteMotor, name = 'data-AutocompleteMotor'),
    path('DadosDeGrafico1', DadosDeGrafico1.as_view(), name= 'data-DadosDeGrafico1'),
]
