
from django.urls import path

from .views import Inicio, SobreView
from .views import PessoaCreate, PessoaUpdate, PessoaDelete, PessoaList 
from .views import MateriaCreate, MateriaUpdate, MateriaDelete, MateriaList
from .views import ConteudoCreate, ConteudoUpdate, ConteudoDelete, ConteudoList
from .views import AssuntoCreate, AssuntoUpdate, AssuntoDelete, AssuntoList
from .views import QuestaoCreate, QuestaoUpdate, QuestaoDelete, QuestaoList

from django.contrib.auth import views as auth_views

urlpatterns = [

    #criar rota para página de login
    path("login/", auth_views.LoginView.as_view(
        template_name = 'paginas/formulario.html',
         extra_context = {
            'titulo': 'Autenticação',
            'botão': 'Entrar'
        }
    ), name="login"),

    #criar uma rota de logout
    path("sair/", auth_views.LogoutView.as_view(), name="logout"),

    path("senha/", auth_views.PasswordChangeView.as_view(
        template_name = 'paginas/formulario.html',
        extra_context = {
            'titulo': 'Atualizar senha',
            'botão': 'Salvar'
        }
    ), name="Senha"),
    



    path("", Inicio.as_view(), name ="index"),
    path("sobre/", SobreView.as_view(), name ="sobre"),

    path('cadastrar/pessoa/', PessoaCreate.as_view(), name="cadastrar-pessoa"),
    path('cadastrar/materia/', MateriaCreate.as_view(), name="cadastrar-materia"),
    path('cadastrar/conteudo/', ConteudoCreate.as_view(), name="cadastrar-conteudo"),
    path('cadastrar/assunto/', AssuntoCreate.as_view(), name="cadastrar-assunto"),
    path('cadastrar/questao/', QuestaoCreate.as_view(), name="cadastrar-questao"),

    path("editar/pessoa/<int:pk>/", PessoaUpdate.as_view(), name= "editar-pessoa"  ),
    path("editar/materia/<int:pk>/", MateriaUpdate.as_view(), name= "editar-materia"  ),
    path("editar/conteudo/<int:pk>/", ConteudoUpdate.as_view(), name= "editar-conteudo"  ),
    path("editar/assunto/<int:pk>/", AssuntoUpdate.as_view(), name= "editar-assunto"  ),
    path("editar/questão/<int:pk>/", QuestaoUpdate.as_view(), name= "editar-questão"  ),

    path("deletar/pessoa/<int:pk>/", PessoaDelete.as_view(), name= "deletar-pessoa"  ),
    path("deletar/materia/<int:pk>/", MateriaDelete.as_view(), name= "deletar-materia"  ),
    path("deletar/conteudo/<int:pk>/", ConteudoDelete.as_view(), name= "deletarr-conteudo"  ),
    path("deletar/assunto/<int:pk>/", AssuntoDelete.as_view(), name= "deletar-assunto"  ),
    path("deletar/questão/<int:pk>/", QuestaoDelete.as_view(), name= "deletar-questão"  ),

     path("listar/pessoa/", PessoaList.as_view(), name="Listar-pessoa"),
     path("listar/materia/", MateriaList.as_view(), name="listar-materia"),
     path("listar/conteudo/", ConteudoList.as_view(), name="Listar-conteudo"),
     path("listar/assunto/", AssuntoList.as_view(), name="Listar-assunto"),
     path("listar/questao/", QuestaoList.as_view(), name="listar-questao" )
]

