"""news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from webapp.views import TemplateLoginView, NewsListTemplateView, NewsCreateView, NewsDetailTemplateView, \
    ArticleUpdateView, ArticleDeleteView, CategoryListTemplateView, CategoryCreateView, CategoryUpdateView, \
    CategoryDeleteView, UserListTemplateView, SignUpView, UserUpdateView, UserDeleteView, logout_view, CategoryView, \
    NewsApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TemplateLoginView.as_view(), name='login'),
    path('sign_up', SignUpView.as_view(), name='sign_up'),
    path('logout/', logout_view, name='logout'),
    path('', NewsListTemplateView.as_view(), name='news'),
    path('news_add/', NewsCreateView.as_view(), name='news_add'),
    path('news_detail/<int:pk>/', NewsDetailTemplateView.as_view(), name='news_detail'),
    path('news_update/<int:pk>/', ArticleUpdateView.as_view(), name='news_update'),
    path('news_delete/<int:pk>/', ArticleDeleteView.as_view(), name='news_delete'),
    path('category_list/', CategoryListTemplateView.as_view(), name='category_list'),
    path('category_add/', CategoryCreateView.as_view(), name='category_add'),
    path('category_update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category_delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('user_list/', UserListTemplateView.as_view(), name='user_list'),
    path('user_update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('user_delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
    path('api/category/', CategoryView.as_view({'get': 'list'})),
    path('api/news/', NewsApiView.as_view({'get': 'list'})),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
