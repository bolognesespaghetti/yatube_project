from django.contrib.auth import get_user_model
from django.db import models


class Group(models.Model):
    """Модель группы. Содержит в себе: название заголовка, слаг, описание."""
    title = models.CharField(
        max_length=200,
        verbose_name='group title'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='group slug'
    )
    description = models.TextField(
        verbose_name='description of the group'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'


User = get_user_model()


class Post(models.Model):
    """
    Модель постов. Содержит в себе: текст поста, дату публикации,
    автора публикации, группу, к который пренадлежит публикация.
    """
    text = models.TextField(verbose_name='post text')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='publication date'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='post author'
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='group',
        verbose_name='publication group'
    )

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ['-pub_date']
