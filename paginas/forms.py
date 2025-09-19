from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Pessoa


class UsuarioCadastroForm(UserCreationForm):
    # Campos do User
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        help_text="Digite um email válido"
    )
    
    # Campos da Pessoa
    nome = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        help_text="Digite seu nome completo"
    )
    
    nascimento = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        }, format='%Y-%m-%d'),
        help_text="Selecione sua data de nascimento"
    )
    
    cidade = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        help_text="Digite sua cidade"
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está em uso.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
            # Criar a Pessoa associada
            Pessoa.objects.create(
                usuario=user,
                nome=self.cleaned_data['nome'],
                nascimento=self.cleaned_data['nascimento'],
                cidade=self.cleaned_data['cidade']
            )
        return user