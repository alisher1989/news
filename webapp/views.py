from collections import OrderedDict

from django.contrib import auth, messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from webapp.forms import ArticleCreateForm, CategoryCreateForm, SignUpForm
from webapp.models import Article, Category
from webapp.serializers import CategorySerializer, ArticleSerializer


class TemplateLoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'registration/login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('news')
        else:
            messages.info(request, 'Неверно введены данные!')
            return redirect('login')


def logout_view(request, *args, **kwargs):
    logout(request)
    return redirect('login')


class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = SignUpForm
        return render(request, 'registration/registration.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        try:
            User.objects.get(username=request.POST.get('username'))
            messages.info(request, 'Такой пользователь уже существует!')
            return redirect('sign_up')
        except Exception:
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                auth.login(request, user)
                return redirect('news')
            else:
                messages.info(request, 'Пароли не совпадают!')
                return redirect('sign_up')


class NewsListTemplateView(ListView):
    model = Article
    template_name = 'news.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        paginator = Paginator(self.get_queryset(), 6, 0)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        context['paginator'] = paginator
        context['page_obj'] = page
        context['news'] = page.object_list
        context['is_paginated'] = page.has_other_pages()
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class NewsDetailTemplateView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'news-detail.html'
    context_object_name = 'new'
    pk_url_kwarg = 'pk'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class NewsCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'news_add.html'
    form_class = ArticleCreateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user
        self.object.save()
        return redirect('news_detail', pk=self.object.pk)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'news_update.html'
    form_class = ArticleCreateForm
    context_object_name = 'new'

    def get_success_url(self):
        return reverse('news_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class ArticleDeleteView(DeleteView):
    model = Article
    pk_kwargs_url = 'pk'
    template_name = 'news_delete.html'
    context_object_name = 'new'
    success_url = reverse_lazy('news')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class CategoryListTemplateView(ListView):
    model = Category
    template_name = 'category_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        paginator = Paginator(self.get_queryset(), 6, 0)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        context['paginator'] = paginator
        context['page_obj'] = page
        context['category_list'] = page.object_list
        context['is_paginated'] = page.has_other_pages()
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class CategoryCreateView(CreateView):
    model = Category
    template_name = 'category_add.html'
    form_class = CategoryCreateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return redirect('category_list')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'category_update.html'
    form_class = CategoryCreateForm
    context_object_name = 'category'

    def get_success_url(self):
        return reverse('category_list')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class CategoryDeleteView(DeleteView):
    model = Category
    pk_kwargs_url = 'pk'
    template_name = 'category_delete.html'
    context_object_name = 'category'
    success_url = reverse_lazy('category_list')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class UserListTemplateView(ListView):
    model = User
    template_name = 'user_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        paginator = Paginator(self.get_queryset(), 6, 0)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        context['paginator'] = paginator
        context['page_obj'] = page
        context['user_list'] = page.object_list
        context['is_paginated'] = page.has_other_pages()
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class UserUpdateView(UpdateView):
    model = User
    template_name = 'user_update.html'
    form_class = SignUpForm
    context_object_name = 'user'

    def get_success_url(self):
        return reverse('user_list')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class UserDeleteView(DeleteView):
    model = User
    pk_kwargs_url = 'pk'
    template_name = 'user_delete.html'
    context_object_name = 'user'
    success_url = reverse_lazy('user_list')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class Pagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page_size'
    max_page_size = 200

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))


class CategoryView(ModelViewSet):
    model = Category
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'pk'


class NewsApiView(ModelViewSet):
    model = Article
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'pk'
    pagination_class = Pagination