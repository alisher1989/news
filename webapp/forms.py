from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from webapp.models import Article, Category


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['category_id', 'title', 'description', 'image']


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'parent_id']


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )