from django.contrib.auth.models import User, AbstractUser
from django.db import models


class Category(models.Model):
    title = models.CharField('Название', max_length=156, null=True, blank=True)
    parent_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='related_category')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return str(self.title)


class Article(models.Model):
    category_id = models.ForeignKey('webapp.Category', on_delete=models.CASCADE, null=True, blank=True, related_name='article_category', verbose_name='Категория')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='user_article', verbose_name='Автор')
    title = models.CharField(max_length=156, null=True, blank=True, verbose_name='Название')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        verbose_name = 'Артикл'
        verbose_name_plural = 'Артиклы'

    def __str__(self):
        return str(self.title)


