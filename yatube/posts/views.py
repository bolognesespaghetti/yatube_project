from django.shortcuts import get_object_or_404, render

from .models import Group, Post

from django.conf import settings


def index(request):
    """Главная страница."""
    template = 'posts/index.html'
    posts = Post.objects.all()[:settings.NUMBER_OF_POSTS]
    context = {
        'posts': posts
    }

    return render(request, template, context)


def group_posts(request, slug):
    """Страница с постами групп."""
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    template = 'posts/group_list.html'
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
