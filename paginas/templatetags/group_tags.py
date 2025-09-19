from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter
def has_group(user, group_names):
    """
    Verifica se o usuário pertence a qualquer um dos grupos especificados.
    Uso: {% if user|has_group:"Administrador,Professor" %}
    """
    if not user.is_authenticated:
        return False
    
    if isinstance(group_names, str):
        group_list = [name.strip() for name in group_names.split(',')]
    else:
        group_list = group_names
    
    user_groups = user.groups.values_list('name', flat=True)
    return any(group in user_groups for group in group_list)

@register.filter
def is_admin_or_professor(user):
    """
    Verifica se o usuário é administrador, professor ou superusuário.
    Uso: {% if user|is_admin_or_professor %}
    """
    if not user.is_authenticated:
        return False
    
    # Superusuário sempre tem acesso
    if user.is_superuser:
        return True
    
    # Verifica se pertence aos grupos Administrador ou Professor
    user_groups = user.groups.values_list('name', flat=True)
    return 'Administrador' in user_groups or 'Professor' in user_groups