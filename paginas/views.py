from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import Pessoa, Materia, Conteudo, Assunto, Questao
from django.contrib.auth.mixins import LoginRequiredMixin
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

class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'

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
class MateriaCreate(LoginRequiredMixin, CreateView):
    model = Materia
    template_name = 'paginas/form.html'
    fields = ['nome']
    success_url = reverse_lazy('listar-materia')
    extra_context = {
        'titulo': 'Cadastrar Matéria',
        'botao': 'Cadastrar',
    }

class MateriaUpdate(LoginRequiredMixin, UpdateView):
    model = Materia
    template_name = 'paginas/form.html'
    fields = ['nome']
    success_url = reverse_lazy('listar-materia')
    extra_context = {
        'titulo': 'Editar Matéria',
        'botao': 'Salvar',
    }

class MateriaDelete(LoginRequiredMixin, DeleteView):
    model = Materia
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-materia')
    extra_context = {
        'titulo': 'Excluir Matéria',
        'botao': 'Excluir',
    }

class MateriaList(LoginRequiredMixin, ListView):
    model = Materia
    template_name = 'listas/materia.html'

# -------------------------------------------
# CRUD Conteúdo
class ConteudoCreate(LoginRequiredMixin, CreateView):
    model = Conteudo
    template_name = 'paginas/form.html'
    fields = ['nome', 'materia']
    success_url = reverse_lazy('listar-conteudo')
    extra_context = {
        'titulo': 'Cadastrar Conteúdo',
        'botao': 'Cadastrar',
    }

class ConteudoUpdate(LoginRequiredMixin, UpdateView):
    model = Conteudo
    template_name = 'paginas/form.html'
    fields = ['nome', 'materia']
    success_url = reverse_lazy('listar-conteudo')
    extra_context = {
        'titulo': 'Editar Conteúdo',
        'botao': 'Salvar',
    }

class ConteudoDelete(LoginRequiredMixin, DeleteView):
    model = Conteudo
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-conteudo')
    extra_context = {
        'titulo': 'Excluir Conteúdo',
        'botao': 'Excluir',
    }

class ConteudoList(LoginRequiredMixin, ListView):
    model = Conteudo
    template_name = 'listas/conteudo.html'

# -------------------------------------------
# CRUD Assunto
class AssuntoCreate(LoginRequiredMixin, CreateView):
    model = Assunto
    template_name = 'paginas/form.html'
    fields = ['nome', 'conteudo']
    success_url = reverse_lazy('listar-assunto')
    extra_context = {
        'titulo': 'Cadastrar Assunto',
        'botao': 'Cadastrar',
    }

class AssuntoUpdate(LoginRequiredMixin, UpdateView):
    model = Assunto
    template_name = 'paginas/form.html'
    fields = ['nome', 'conteudo']
    success_url = reverse_lazy('listar-assunto')
    extra_context = {
        'titulo': 'Editar Assunto',
        'botao': 'Salvar',
    }

class AssuntoDelete(LoginRequiredMixin, DeleteView):
    model = Assunto
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-assunto')
    extra_context = {
        'titulo': 'Excluir Assunto',
        'botao': 'Excluir',
    }

class AssuntoList(LoginRequiredMixin, ListView):
    model = Assunto
    template_name = 'listas/assunto.html'

# -------------------------------------------
# CRUD Questão
class QuestaoCreate(LoginRequiredMixin, CreateView):
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

class QuestaoUpdate(LoginRequiredMixin, UpdateView):
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

class QuestaoDelete(LoginRequiredMixin, DeleteView):
    model = Questao
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-questao')
    extra_context = {
        'titulo': 'Excluir Questão',
        'botao': 'Excluir',
    }

    def get_object(self, queryset=None):
        return get_object_or_404(Questao, pk=self.kwargs['pk'], cadastrada_por=self.request.user)

class QuestaoList(LoginRequiredMixin, ListView):
    model = Questao
    template_name = 'listas/questao.html'

class MinhasQuestoes(QuestaoList):
    def get_queryset(self):
        return Questao.objects.filter(cadastrada_por=self.request.user)