from rest_framework import serializers

from webapp.models import Category, Article


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = []


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = []