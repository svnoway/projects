from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from main.models import Datask


class Task(ListView):
    model = Datask
    context_object_name = "taski"

class TaskDetail(DetailView):
    model = Datask
    context_object_name = 'task'
    template_name = 'main/task.html'

class TaskCreate(CreateView):
    model = Datask
    fields = '__all__'
    template_name = 'main/create.html'
    success_url = reverse_lazy('tasklist')

class TaskUpdate(UpdateView):
    model = Datask
    fields = '__all__'
    template_name = 'main/create.html'
    success_url = reverse_lazy('tasklist')

class TaskDelete(DeleteView):
    model = Datask
    fields = '__all__'
    context_object_name = 'taski'
    success_url = reverse_lazy('tasklist')
    template_name = 'main/delete.html'



