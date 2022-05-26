from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.


class PostNewsList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'news.html'
    context_object_name = 'news'


class PostNewsDetail(DetailView):
    model = Post
    template_name = 'one_news.html'
    context_object_name = 'news'
