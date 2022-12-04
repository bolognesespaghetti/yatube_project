from django.contrib.auth import get_user_model
from django.db import models


class Group(models.Model):
    """Модель группы. Содержит в себе: название заголовка, слаг, описание."""
    title = models.CharField(
        max_length=200,
        verbose_name='название группы'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='слаг группы'
    )
    description = models.TextField(
        verbose_name='описание группы'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'группы'


User = get_user_model()


class Post(models.Model):
    """
    Модель постов. Содержит в себе: текст поста, дату публикации,
    автора публикации, группу, к которой пренадлежит публикация.
    """
    text = models.TextField(
        verbose_name='текст поста'
        )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата публикации'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='автор поста'
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='группа публикации'
    )

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        ordering = ['-pub_date']
