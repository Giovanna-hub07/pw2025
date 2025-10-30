from django.urls import path
from django.contrib.auth import views as auth_views

from .views import (
    InicioView, SobreView, CadastroUsuarioView,
    PessoaCreate, PessoaUpdate, PessoaDelete, PessoaList,
    MateriaCreate, MateriaUpdate, MateriaDelete, MateriaList,
    ConteudoCreate, ConteudoUpdate, ConteudoDelete, ConteudoList,
    AssuntoCreate, AssuntoUpdate, AssuntoDelete, AssuntoList,
    QuestaoCreate, QuestaoUpdate, QuestaoDelete, QuestaoList, MinhasQuestoes, QuestaoDetail

)

urlpatterns = [

    # Página inicial e sobre
    path("", InicioView.as_view(), name="index"),
    path("sobre/", SobreView.as_view(), name="sobre"),

    # Autenticação
    path("login/", auth_views.LoginView.as_view(
        template_name='paginas/form.html',
        extra_context={
            'titulo': 'Autenticação',
            'botao': 'Entrar'
        }
    ), name="login"),

    path("sair/", auth_views.LogoutView.as_view(), name="logout"),

    path("alterar-senha/", auth_views.PasswordChangeView.as_view(
        template_name='paginas/form.html',
        success_url='/',
        extra_context={
            'titulo': 'Atualizar senha',
            'botao': 'Salvar'
        }
    ), name="alterar-senha"),

    # Registro de novos usuários
    path("registrar/", CadastroUsuarioView.as_view(), name="registrar"),

    # Pessoa
    path("cadastrar/pessoa/", PessoaCreate.as_view(), name="cadastrar-pessoa"),
    path("editar/pessoa/<int:pk>/", PessoaUpdate.as_view(), name="editar-pessoa"),
    path("excluir/pessoa/<int:pk>/", PessoaDelete.as_view(), name="excluir-pessoa"),
    path("listar/pessoa/", PessoaList.as_view(), name="listar-pessoa"),

    # Matéria
    path("cadastrar/materia/", MateriaCreate.as_view(), name="cadastrar-materia"),
    path("editar/materia/<int:pk>/",
         MateriaUpdate.as_view(), name="editar-materia"),
    path("excluir/materia/<int:pk>/",
         MateriaDelete.as_view(), name="excluir-materia"),
    path("listar/materia/", MateriaList.as_view(), name="listar-materia"),

    # Conteúdo
    path("cadastrar/conteudo/", ConteudoCreate.as_view(),
         name="cadastrar-conteudo"),
    path("editar/conteudo/<int:pk>/",
         ConteudoUpdate.as_view(), name="editar-conteudo"),
    path("excluir/conteudo/<int:pk>/",
         ConteudoDelete.as_view(), name="excluir-conteudo"),
    path("listar/conteudo/", ConteudoList.as_view(), name="listar-conteudo"),

    # Assunto
    path("cadastrar/assunto/", AssuntoCreate.as_view(), name="cadastrar-assunto"),
    path("editar/assunto/<int:pk>/",
         AssuntoUpdate.as_view(), name="editar-assunto"),
    path("excluir/assunto/<int:pk>/",
         AssuntoDelete.as_view(), name="excluir-assunto"),
    path("listar/assunto/", AssuntoList.as_view(), name="listar-assunto"),

    # Questão
    path("cadastrar/questao/", QuestaoCreate.as_view(), name="cadastrar-questao"),
    path("editar/questao/<int:pk>/",
         QuestaoUpdate.as_view(), name="editar-questao"),
    path("excluir/questao/<int:pk>/",
         QuestaoDelete.as_view(), name="excluir-questao"),
    path("listar/questao/", QuestaoList.as_view(), name="listar-questao"),
    path("questao/<int:pk>/", QuestaoDetail.as_view(), name="detalhe-questao"),

    # Minhas Questões (apenas do usuário logado)
    path("listar/minhas-questoes/",
         MinhasQuestoes.as_view(), name="minhas-questoes"),
]
