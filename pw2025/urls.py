"""
URL configuration for pw2025 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.contrib import IndexView, SobreView
from django.urls import path, include
from views import IndexView, MateriaCreate, ConteudoCreate, AssuntoCreate, QuestaoCreate


urlpatterns = [

    path('', IndexView.as_view(), name= 'index'), 
    path("sobre/", SobreView.as_views(), name="sobre"),
    
    path('cadastrar/materia/', MateriaCreate.as_view(), name="cadastrar-materia"),
    path('cadastrar/conteudo/', ConteudoCreate.as_view(), name="cadastrar-conteudo"),
    path('cadastrar/assunto/', AssuntoCreate.as_view(), name="cadastrar-assunto"),
    path('cadastrar/questao/', QuestaoCreate.as_view(), name="cadastrar-questao"),
]

    


