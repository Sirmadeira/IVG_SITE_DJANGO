"""IVG_SITE_DJANGO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from usuarios import views as usuarios_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Cadastro/', usuarios_views.Cadastro, name= 'Cadastro'),
    path('Empresa/', usuarios_views.Empresa, name= 'Empresa'),
    path('Login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name= 'Login'),
    path('Logout/', auth_views.LogoutView.as_view(template_name='usuarios/logout.html'), name= 'Logout'),
    path('', include('APP_IVG.urls')),
]
