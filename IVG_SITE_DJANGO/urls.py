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
from usuarios.forms import UserLoginForm, CustomResetForm
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Essas view seria a dos administradores
    path('admin/', admin.site.urls),

    #Essas views sao relacionadas o usuario
    path('Cadastro/', usuarios_views.Cadastro, name= 'Cadastro'),
    path('Empresa/', usuarios_views.Empresa, name= 'Empresa'),
    path('Login/', auth_views.LoginView.as_view(template_name='usuarios/login.html',authentication_form= UserLoginForm), name= 'Login'),
    path('Logout/', auth_views.LogoutView.as_view(template_name='usuarios/logout.html'), name= 'Logout'),

    #Essas views estao em minusculo porque django e chato, e nao aceita views de reset com primeira letra maiuscula
     path('password-reset/',
         auth_views.PasswordResetView.as_view(
            # Templates para o email de reset de usuarios
             template_name='usuarios/password_reset.html',
             email_template_name='usuarios/password_reset_email.html',
             subject_template_name='usuarios/password_reset_subject.txt'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='usuarios/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='usuarios/password_reset_confirm.html',
             form_class=CustomResetForm
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='usuarios/password_reset_complete.html'
         ),
         name='password_reset_complete'),

    # Path para principal
    path('', include('APP_IVG.urls')),
    # Views para dados
    path('Data/', include('data.urls')),
    path('DataC/', include('datac.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

