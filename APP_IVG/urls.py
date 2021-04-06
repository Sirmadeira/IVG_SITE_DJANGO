from django.urls import path
from .import views

urlpatterns = [
    path('', views.Homepage, name = 'APP_IVG-Homepage'),
    path('Sobre/', views.Sobre, name = 'APP_IVG-Sobre'),
    path('Faq/', views.Faq, name = 'APP_IVG-Faq'),
]