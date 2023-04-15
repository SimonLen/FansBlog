from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

from .config.post_categories import CATEGORIES


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=16, verbose_name='username')


class Post(models.Model):
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=64, verbose_name='Заголовок')
    content = RichTextField()
    created_at = models.DateTimeField(auto_created=True, verbose_name='Дата и время создания')
    category = models.CharField(max_length=16, choices=CATEGORIES, verbose_name='Категория')
    likes = models.ManyToManyField(Author, blank=True, related_name='liked_posts')
    dislikes = models.ManyToManyField(Author, blank=True, related_name='disliked_posts')


class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.CharField(max_length=1024,verbose_name='Сообщение')
    likes = models.ManyToManyField(Author, blank=True, related_name='liked_comments')
    dislikes = models.ManyToManyField(Author, blank=True, related_name='disliked_comments')
