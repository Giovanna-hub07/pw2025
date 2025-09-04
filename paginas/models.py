from django.db import models
from django.contrib.auth.models import User



class Pessoa(models.Model):
    nome = models.CharField(
        max_length=50, verbose_name="Qual o seu nome?", help_text="Digite seu nome completo"
    )
    nascimento = models.DateField(verbose_name="Data de nascimento")
    cidade = models.CharField(max_length=100)
    usuario = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='pessoa'
    )
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.nascimento})"

    class Meta:
        ordering = ['nome']



class Materia(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da matéria")
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']


class Conteudo(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do conteúdo")
    materia = models.ForeignKey(Materia, on_delete=models.PROTECT)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.materia}"

    class Meta:
        ordering = ['nome', 'materia']


class Assunto(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do assunto")
    conteudo = models.ForeignKey(Conteudo, on_delete=models.PROTECT)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.conteudo}"

    class Meta:
        ordering = ['nome', 'conteudo']


class Questao(models.Model):
    descricao = models.TextField(verbose_name="Enunciado da questão")
    resolucao = models.TextField(verbose_name="Resolução da questão")
    assunto = models.ForeignKey(Assunto, on_delete=models.PROTECT)
    cadastrada_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    cadastrada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Questão sobre: {self.assunto}"

    class Meta:
        ordering = ['assunto']
