from django.views.generic import TemplateView, ListView
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
    fields = ['nome', 'nascimento', 'email', 'cidade']
    template_name = 'paginas/formulario.html'
    success_url = reverse_lazy('listar-pessoa')
    extra_context = {
        'titulo': 'Cadastrar Pessoa',
        'botão': 'Cadastrar'
    }


class PessoaUpdate(UpdateView):
    model = Pessoa
    fields = ['nome', 'nascimento', 'email', 'cidade']
    template_name = 'paginas/formulario.html'
    success_url = reverse_lazy('listar-pessoa')
    extra_context = {
        'titulo': 'Atualização do cadastro de dados da Pessoa',
        'botão': 'Salvar'
    }



class PessoaDelete(DeleteView):
    model = Pessoa
    template_name = 'paginas/formulario.html'
    success_url = reverse_lazy('listar-pessoa')


########################################################################


class MateriaCreate(CreateView):
    model = Materia
    fields = ['nome']
    template_name = 'paginas/formulario.html'
    success_url = reverse_lazy('listar-materia')
    extra_context = {
        'titulo': 'Cadastrar Matéria',
        'botão': 'Cadastrar'
    }


class MateriaUpdate(UpdateView):
    model = Materia
    fields = ['nome']
    template_name = 'paginas/formulario.html'
    success_url = reverse_lazy('listar-materia')
     


class MateriaDelete(DeleteView):
    model = Materia
    template_name = 'paginas/formulario.html'
    success_url = reverse_lazy('listar-materia')


########################################################################


class ConteudoCreate(CreateView):
    model = Conteudo
    fields = ['nome', 'materia']
    template_name = 'paginas/formulario.html'
    success_url = reverse_lazy('listar-conteudo')
    extra_context = {
        'titulo': 'Cadastrar Conteudo',
        'botão': 'Cadastrar'
    }



class ConteudoUpdate(UpdateView):
    model = Conteudo
    fields = ['nome', 'materia']
    template_name = 'paginas/formulario.html'
    success_url = reverse_lazy('listar-conteudo')


class ConteudoDelete(DeleteView):
    model = Conteudo
    template_name = 'paginas/formulario.html'
    success_url = reverse_lazy('listar-conteudo')


########################################################################


class AssuntoCreate(CreateView):
    model = Assunto
    fields = ['nome', 'conteudo']
    template_name = 'paginas/formulario.html'
    success_url = reverse_lazy('listar-assunto')
    extra_context = {
        'titulo': 'Cadastar Assunto ',
        'botão': 'Cadastrar'
    }


class AssuntoUpdate(UpdateView):
    model = Assunto
    fields = ['nome', 'conteudo']
    template_name = 'paginas/formulario.html'
    success_url = reverse_lazy('listar-assunto')


class AssuntoDelete(DeleteView):
    model = Assunto
    template_name = 'paginas/formulario.html'
    success_url = reverse_lazy('listar-assunto')


########################################################################


class QuestaoCreate(CreateView):
    model = Questao
    fields = ['descricao', 'resolucao', 'assunto', 'cadastrada_por']
    template_name = 'paginas/formulario.html'
    success_url = reverse_lazy('listar-questao')
    extra_context = {
        'titulo': 'Cadastar Questões ',
        'botão': 'Cadastrar'
    }


class QuestaoUpdate(UpdateView):
    model = Questao
    fields = ['descricao', 'resolucao', 'assunto', 'cadastrada_por']
    template_name = 'paginas/formulario.html'
    success_url = reverse_lazy('listar-questao')


class QuestaoDelete(DeleteView):
    model = Questao
    template_name = 'paginas/formulario.html'
    success_url = reverse_lazy('listar-questao')


    ########################################################################


class PessoaList(ListView):
    model = Pessoa
    template_name = 'paginas/Listas/pessoa.html'


class MateriaList(ListView):
    model = Materia
    template_name = 'paginas/materia.html'


class ConteudoList(ListView):
    model = Conteudo
    template_name = 'paginas/conteudo.html'

class AssuntoList(ListView):
    model = Assunto
    template_name = 'paginas/assunto.html'

class QuestaoList(ListView):
    model = Questao
    template_name = 'paginas/questao.html'

