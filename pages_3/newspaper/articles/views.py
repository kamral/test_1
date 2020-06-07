# articles/views.py
from django.views.generic import (
    ListView,
    DetailView
)# new
from django.views.generic.edit import (
    UpdateView,
    DeleteView,
    CreateView
)# new
from django.urls import reverse_lazy # new
from .models import Article
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html'
    paginate_by = 2
    queryset = Article.objects.all()


class ArticleDetailView(LoginRequiredMixin, DetailView): # new
    model = Article
    template_name = 'article_detail.html'

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin,  UpdateView): # new
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'
    login_url = 'login'

    def test_func(self):
        obj=self.get_object()
        return obj.author==self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # new
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    def test_func(self):
        obj=self.get_object()
        return obj.author==self.request.user


class ArticleCreativeView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body', 'author')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
