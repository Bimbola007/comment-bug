from django.shortcuts import render

from .models import Articles, Comments
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

class ArticlesList(LoginRequiredMixin,ListView):
    model = Articles
    template_name = 'articles_list.html'

class ArticleDetailedView(LoginRequiredMixin,DetailView):
    model = Articles
    template_name = 'Article_detail.html'

class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Articles
    template_name = 'Article_edit.html'
    fields = ['title', 'body']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user



class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Articles
    template_name = 'Article_delete.html'
    success_url = reverse_lazy('articles_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user



class CreateNewArticle(LoginRequiredMixin,CreateView):
    model = Articles
    template_name = 'Article_new.html'
    fields = ('title','body')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CreateNewComment(CreateView):
    model = Comments
    template_name = 'New_Comment.html'
    fields = ['author', 'article', 'comment']