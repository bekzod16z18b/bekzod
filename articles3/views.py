
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Articles3

class Artic3leListView(ListView):
    model = Articles3
    template_name = 'articles3_list.html'

class Artic3leDetailView(DetailView):
    model = Articles3
    template_name = 'articles3_detail.html'

class Artic3leUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articles3
    fields = ('title', 'body',)
    template_name = 'articles3_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class Artic3leDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articles3
    template_name = 'articles3_delete.html'
    success_url = reverse_lazy('articles3_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class Artic3leCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Articles3
    template_name = 'articles3_new.html'
    fields = ('title','body',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user superuser ekanini tekshirish
    def test_func(self):
        return self.request.user.is_superuser