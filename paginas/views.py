from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import  Pessoa, Materia, Conteudo, Assunto, Questao


# função que converte o nome de uma url na rota dela



class Inicio(TemplateView):
    template_name = "paginas/index.html"

class SobreView(TemplateView):
    template_name = "paginas/sobre.html"
    
class PessoaCreate(CreateView):
    model = Pessoa
    fields = ['nome', 'nascimento', 'email', 'cideda']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('index')


class PessoaUpdate(UpdateView):
    model = Pessoa
    fields = ['nome', 'nascimento', 'email', 'cideda']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('index')


class PessoaDelete(DeleteView):
    model = Pessoa
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('index')



class MateriaCreate(CreateView):
    model = Materia
    fields = ['nome']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('index')


class MateriaUpdate(UpdateView):
    model = Materia
    fields = ['nome']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('index')


class MateriaDelete(DeleteView):
    model = Materia
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('index')


class ConteudoCreate(CreateView):
    model = Conteudo
    fields = ['nome', 'materia']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('index')


class ConteudoUpdate(UpdateView):
    model = Conteudo
    fields = ['nome', 'materia']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('index')


class ConteudoDelete(DeleteView):
    model = Conteudo
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('index')



class AssuntoCreate(CreateView):
    model = Assunto
    fields = ['nome', 'conteudo']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('index')


class AssuntoUpdate(UpdateView):
    model = Assunto
    fields = ['nome', 'conteudo']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('index')


class AssuntoDelete(DeleteView):
    model = Assunto
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('index')



class QuestaoCreate(CreateView):
    model = Questao
    fields = ['descricao', 'resolucao', 'assunto', 'cadastrada_por']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('index')


class QuestaoUpdate(UpdateView):
    model = Questao
    fields = ['descricao', 'resolucao', 'assunto', 'cadastrada_por']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('index')


class QuestaoDelete(DeleteView):
    model = Questao
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('index')