<body>
  <header class="site-header">
      <nav class="navbar navbar-expand-lg navbar-dark bg-steel fixed-top mx-auto p-0">
        <div class="container">
          <a class="navbar-brand" style="height: 100px; margin: 10px;" href="/HomePage"><img src="{{ url_for('static', filename='imagens/Logo-IVG-azulclaro.png')}}" class="logo" alt="marca da IVG"></a>
          <button class="navbar-toggler text-center" type="button" data-toggle="collapse" data-target="#navbarToggle" aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarToggle">
            <div class="navbar-nav">
              <a class="nav-item nav-link active" href="{{ url_for('Principal.HomePage') }}"> Home</a>
              <a class="nav-item nav-link active" href="{{ url_for('Principal.Sobre') }}"> Sobre</a>
              <a class="nav-item nav-link active" href="{{ url_for('Principal.Faq') }}"> Faq</a>
            </div>
            <!-- Navbar Right Side -->
            <div class="navbar-nav">
              {% if current_user.is_authenticated %}
                <a class="nav-item nav-link active" href="{{ url_for('Usuarios.ContaEmpresa') }}">Empresa</a>
                <a class="nav-item nav-link active" href="{{ url_for('Tabelas.SegundaJanela') }}">Inserir dados</a>
                <a class="nav-item nav-link active" href="{{ url_for('Tabelas.TerceiraJanela') }}">Visualizar dados</a>
                <a class="nav-item nav-link active" href="{{ url_for('Usuarios.Logout') }}">Logout</a>
                <div class="nav-item nav-link active">
                <a class="btn btn-info mx-auto mr-4 d-none" data-toggle="collapse" href="#collapseExample" role="button" aria-expanded="false" aria-controls="collapseExample"><img src="{{ url_for('static', filename='imagens/Homepage-Pesquisar.png')}}" style="height: 24px; width: auto;"></img></a>
                </div>
              {% else %}
                <a class="nav-item nav-link active" href="{{ url_for('Usuarios.Login') }}">Login</a>
                <a class="nav-item nav-link active" href="{{ url_for('Usuarios.Cadastro') }}">Cadastro</a>
              {% endif %}
            </div> 
          </div>
        </div>
      </nav>
       <!-- Área de Pesquisa, deixar desligada por enquanto -->
    <div class="collapse d-none" id="collapseExample">
          <div class="card card-body bg-dark p-4 d-none" style="width: 100%; height: 700px; opacity: .9; position: relative;">
         <input class="my-auto p-4 d-none" type="search" placeholder="Pesquisar" aria-label="Search" name="search" style="font-size: 30px; letter-spacing: 2px; margin: auto 60px;">
          </div>
    </div>
  </header>
  <main role="main" class="container-fluid m-0">
    <div class="row">
        <div class="col">
          {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
              {% for category , message in messages%}
                <div class = "alert alert-{{ category}} mt-4">
                  {{ message }}
                </div>
              {% endfor %}
            {% endif %}
          {% endwith %}
          {% block content%}{% endblock %}
        </div>
      </div>
    </main>
  <footer class="footer bg-dark text-white py-1 mb-0" style="position: absolute; width: 100%; min-height: 160px;">
      <div class="container text-center mt-1">
      <div class="row">
      <div class="col-xl my-auto py-auto">
        <ul  style="list-style: none; font-size: 14px; padding: 0 0; display: inline-flex;">
            <li><a href="{{('https://www.facebook.com/ivgtecnologiadedados')}}" target="_blank"><img src="{{ url_for('static', filename='imagens/Footer-Facebook.png')}}" class="redesocial"></a></li> 
            <li><a href="{{('https://twitter.com/ivgtech')}}" target="_blank"><img src="{{ url_for('static', filename='imagens/Footer-Twitter.png')}}" class="redesocial2"></a></li> 
            <li><a href="{{('https://www.linkedin.com/company/ivgtecnologia-de-dados/about/?viewAsMember=true')}}" target="_blank">
                  <img src="{{ url_for('static', filename='imagens/Footer-Linkedin.png')}}"  class="redesocial">
                </a>
            </li>
        </ul>
      </div>
        <div class="col-xl my-auto py-auto">
        <ul class="text-uppercase" style="list-style: none; font-size: 14px; padding: 0;">
             <li>Ivg Tecnologia de Dados - Todos os Direitos Reservados</li> 
             <li>2021</li> 
        </ul>
        </div>
       <div class="col-xl my-auto py-auto">
        <ul  style="list-style: none; font-size: 12px; padding: 0; margin-top: 20px;">
             <li>Rua Livio Edmondo Levi, 25</li> 
             <li>Cep: 056.92-160</li> 
             <li>Bairro Morumbi, SP Capital</li>
             <li>TEL.: (11) 97498-4826</li>
             <li> SAC: ivgtecnologia@gmail.com</li>
        </ul>
       </div>
    </footer>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
</body>
</html>"""IVG_SITE_DJANGO URL Configuration

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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('APP_IVG.urls')),
]
