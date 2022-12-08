from django import template

register = template.Library()


@register.filter
def addclass(field, css):
    """Добавляет в html-шаблон атрибут класса."""
    return field.as_widget(attrs={'class': css})
