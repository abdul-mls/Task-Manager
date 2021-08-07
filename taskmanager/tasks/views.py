from django.shortcuts import render, redirect
from .models import *

from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView, FormView)
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'tasks/login.html'
    fields = '__all__'

    # restricting user to go on "login" page if he is already logged in
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('task_list')


class RegisterView(FormView):
    template_name = 'tasks/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    # refusing access to 'login' and 'register' page to user, as user already logged in
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('task_list')
        return super(RegisterView, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    # filtering data, so that logged user can only see his own data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains=search_input)

        context['search_input'] = search_input

        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'importance', 'creation_date', 'ending_date', 'complete']
    success_url = reverse_lazy('task_list')

    # assigning logged user to the tasks he creates
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('task_list')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')

