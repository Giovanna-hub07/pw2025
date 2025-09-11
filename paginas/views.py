from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import Pessoa, Materia, Conteudo, Assunto, Questao
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.contrib.auth.models import User
# from .forms import UsuarioCadastroForm

# -------------------------------------------
# Cadastro de Usuário
# class CadastroUsuarioView(CreateView):
#     model = User
#     form_class = UsuarioCadastroForm
#     template_name = 'paginas/form.html'
#     success_url = reverse_lazy('login')
#     extra_context = {
#         'titulo': 'Cadastro de Usuário',
#         'botao': 'Cadastrar',
#     }

# Páginas estáticas
class InicioView(TemplateView):
    template_name = 'paginas/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["quantidade_questoes"] = Questao.objects.all().count()
        context["quantidade_conteudo"] = Conteudo.objects.all().count()
        context["quantidade_assunto"] = Assunto.objects.all().count()
        return context

class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'
''
# -------------------------------------------
# CRUD Pessoa
class PessoaCreate(LoginRequiredMixin, CreateView):
    model = Pessoa
    template_name = 'paginas/form.html'
    fields = ['nome', 'nascimento', 'cidade']
    success_url = reverse_lazy('listar-pessoa')
    extra_context = {
        'titulo': 'Cadastrar Pessoa',
        'botao': 'Cadastrar',
    }

class PessoaUpdate(LoginRequiredMixin, UpdateView):
    model = Pessoa
    template_name = 'paginas/form.html'
    fields = ['nome', 'nascimento', 'cidade']
    success_url = reverse_lazy('listar-pessoa')
    extra_context = {
        'titulo': 'Editar Pessoa',
        'botao': 'Salvar',
    }

class PessoaDelete(LoginRequiredMixin, DeleteView):
    model = Pessoa
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-pessoa')
    extra_context = {
        'titulo': 'Excluir Pessoa',
        'botao': 'Excluir',
    }

class PessoaList(LoginRequiredMixin, ListView):
    model = Pessoa
    template_name = 'listas/pessoa.html'

# -------------------------------------------
# CRUD Matéria
class MateriaCreate(GroupRequiredMixin, CreateView):
    group_required = ["Administrador", "Professor"]
    model = Materia
    template_name = 'paginas/form.html'
    fields = ['nome']
    success_url = reverse_lazy('listar-materia')
    extra_context = {
        'titulo': 'Cadastrar Matéria',
        'botao': 'Cadastrar',
    }

class MateriaUpdate(GroupRequiredMixin, UpdateView):
     group_required = ["Administrador", "Professor"]
     model = Materia
     template_name = 'paginas/form.html'
     fields = ['nome']
     success_url = reverse_lazy('listar-materia')
     extra_context = {
        'titulo': 'Editar Matéria',
        'botao': 'Salvar',
    }

class MateriaDelete(GroupRequiredMixin, DeleteView):
    group_required = ["Administrador", "Professor"]
    model = Materia
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-materia')
    extra_context = {
        'titulo': 'Excluir Matéria',
        'botao': 'Excluir',
    }

class MateriaList(GroupRequiredMixin, ListView):
    group_required = ["Administrador", "Professor"]
    model = Materia
    template_name = 'listas/materia.html'

# -------------------------------------------
# CRUD Conteúdo
class ConteudoCreate(GroupRequiredMixin, CreateView):
    group_required = ["Administrador", "Professor"]
    model = Conteudo
    template_name = 'paginas/form.html'
    fields = ['nome', 'materia']
    success_url = reverse_lazy('listar-conteudo')
    extra_context = {
        'titulo': 'Cadastrar Conteúdo',
        'botao': 'Cadastrar',
    }

class ConteudoUpdate(GroupRequiredMixin, UpdateView):
    group_required = ["Administrador", "Professor"]
    model = Conteudo
    template_name = 'paginas/form.html'
    fields = ['nome', 'materia']
    success_url = reverse_lazy('listar-conteudo')
    extra_context = {
        'titulo': 'Editar Conteúdo',
        'botao': 'Salvar',
    }

class ConteudoDelete(GroupRequiredMixin, DeleteView):
    group_required = ["Administrador", "Professor"]
    model = Conteudo
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-conteudo')
    extra_context = {
        'titulo': 'Excluir Conteúdo',
        'botao': 'Excluir',
    }

class ConteudoList(GroupRequiredMixin, ListView):
    group_required = ["Administrador", "Professor"]
    model = Conteudo
    template_name = 'listas/conteudo.html'

# -------------------------------------------
# CRUD Assunto
class AssuntoCreate(GroupRequiredMixin, CreateView):
    group_required = ["Administrador", "Professor"]
    model = Assunto
    template_name = 'paginas/form.html'
    fields = ['nome', 'conteudo']
    success_url = reverse_lazy('listar-assunto')
    extra_context = {
        'titulo': 'Cadastrar Assunto',
        'botao': 'Cadastrar',
    }

class AssuntoUpdate(GroupRequiredMixin, UpdateView):
    group_required = ["Administrador", "Professor"]
    model = Assunto
    template_name = 'paginas/form.html'
    fields = ['nome', 'conteudo']
    success_url = reverse_lazy('listar-assunto')
    extra_context = {
        'titulo': 'Editar Assunto',
        'botao': 'Salvar',
    }

class AssuntoDelete(GroupRequiredMixin, DeleteView):
    group_required = ["Administrador", "Professor"]
    model = Assunto
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-assunto')
    extra_context = {
        'titulo': 'Excluir Assunto',
        'botao': 'Excluir',
    }

class AssuntoList(GroupRequiredMixin, ListView):
    group_required = ["Administrador", "Professor"]
    model = Assunto
    template_name = 'listas/assunto.html'

# -------------------------------------------
# CRUD Questão
class QuestaoCreate(GroupRequiredMixin, CreateView):
    group_required = ["Administrador", "Professor"]
    model = Questao
    template_name = 'paginas/form.html'
    fields = ['descricao', 'resolucao', 'assunto']
    success_url = reverse_lazy('listar-questao')
    extra_context = {
        'titulo': 'Cadastrar Questão',
        'botao': 'Cadastrar',
    }

    def form_valid(self, form):
        form.instance.cadastrada_por = self.request.user
        return super().form_valid(form)

class QuestaoUpdate(GroupRequiredMixin, UpdateView):
    group_required = ["Administrador", "Professor"]
    model = Questao
    template_name = 'paginas/form.html'
    fields = ['descricao', 'resolucao', 'assunto']
    success_url = reverse_lazy('listar-questao')
    extra_context = {
        'titulo': 'Editar Questão',
        'botao': 'Salvar',
    }

    def get_object(self, queryset=None):
        return get_object_or_404(Questao, pk=self.kwargs['pk'], cadastrada_por=self.request.user)

class QuestaoDelete(GroupRequiredMixin, DeleteView):
    group_required = ["Administrador", "Professor"]
    model = Questao
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-questao')
    extra_context = {
        'titulo': 'Excluir Questão',
        'botao': 'Excluir',
    }

    def get_object(self, queryset=None):
        return get_object_or_404(Questao, pk=self.kwargs['pk'], cadastrada_por=self.request.user)

class QuestaoList(GroupRequiredMixin, ListView):
    group_required = ["Administrador", "Professor"]
    model = Questao
    template_name = 'listas/questao.html'



class MinhasQuestoes(LoginRequiredMixin, ListView):
    model = Questao
    template_name = 'listas/questao.html'
    def get_queryset(self):
        model = Questao
        template_name = 'listas/questao.html'

        return Questao.objects.filter(cadastrada_por=self.request.user)
    
