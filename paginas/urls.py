
from django.urls import path

from .views import Inicio, SobreView
from .views import PessoaCreate, PessoaUpdate, PessoaDelete
from .views import MateriaCreate, MateriaUpdate, MateriaDelete
from .views import ConteudoCreate, ConteudoUpdate, ConteudoDelete
from .views import AssuntoCreate, AssuntoUpdate, AssuntoDelete
from .views import QuestaoCreate, QuestaoUpdate, QuestaoDelete

urlpatterns = [

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



]

