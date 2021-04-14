from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from main.models import Datask


class Login(LoginView):
    template_name = 'main/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasklist')


class RegisterPage(FormView):
    template_name = 'main/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasklist')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)


class Task(LoginRequiredMixin, ListView):
    model = Datask
    context_object_name = "taski"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['taski'] = context['taski'].filter(user=self.request.user)
        context['count'] = context['taski'].filter(complete=False).count()
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['taski']= context['taski'].filter(
                title__icontains=search_input)
        context['search_input'] = search_input
        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Datask
    context_object_name = 'task'
    template_name = 'main/task.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Datask
    fields = ['title', 'description', 'complete']
    template_name = 'main/create.html'
    success_url = reverse_lazy('tasklist')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Datask
    fields = ['title', 'description', 'complete']
    template_name = 'main/create.html'
    success_url = reverse_lazy('tasklist')

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Datask
    fields = '__all__'
    context_object_name = 'taski'
    success_url = reverse_lazy('tasklist')
    template_name = 'main/delete.html'

