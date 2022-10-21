
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Practical

class PracticalListView(ListView):
    model = Practical
    template_name = 'practical_list.html'

class PracticalDetailView(DetailView):
    model = Practical
    template_name = 'practical_detail.html'

class PracticalUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Practical
    fields = ('title','body',)
    template_name = 'practical_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class PracticalDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Practical
    template_name = 'practical_delete.html'
    success_url = reverse_lazy('practical_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class PracticalCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Practical
    template_name = 'practical_new.html'
    fields = ('title','body',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user superuser ekanini tekshirish
    def test_func(self):
        return self.request.user.is_superuser