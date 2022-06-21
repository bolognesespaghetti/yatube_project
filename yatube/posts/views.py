from django.shortcuts import get_object_or_404, render

from .models import Group, Post

from django.conf import settings


def index(request):
    """Главная страница."""
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    posts = Post.objects.all()[:settings.NUMBER_OF_POSTS]
    context = {
        'title': title,
        'posts': posts
    }

    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.group.all()
    title = 'Записи сообщества ' + group.title
    template = 'posts/group_list.html'
    context = {
        'group': group,
        'posts': posts,
        'title': title
    }
    return render(request, template, context)
