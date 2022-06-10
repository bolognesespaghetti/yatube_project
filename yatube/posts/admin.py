from django.contrib import admin

from .models import Group, Post


class PostAdmin(admin.ModelAdmin):
    # Поля в админке
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group'
    )

    # Интерфейс изминения группы
    list_editable = ('group',)
    # Интерфейс для поиска по тексту постов
    search_fields = ('text',)
    # Фильтрация по дате
    list_filter = ('pub_date',)
    # Пустое поле, если в графе ничего нет
    empty_value_display = '-empty-'


# Регистрация конфигуратора PostAdmin для модели Post
admin.site.register(Post, PostAdmin)

# Регистрация модели Group
admin.site.register(Group)
