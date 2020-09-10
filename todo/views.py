#
from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView, TemplateView

from todo.forms import TodoForm
from todo.models import Todo, Category


class TodoIndexView(ListView):
    model = Todo
    template_name = 'todo/index.html'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.order_by('pk').all()
        return context

    def get_queryset(self):
        object_list = Todo.objects.order_by('pk').all()
        return object_list


class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo/detail.html'
    form_class = TodoForm


class TodoCreateView(CreateView, ListView):
    model = Todo
    template_name = "todo/create.html"
    form_class = TodoForm
    success_url = reverse_lazy('todo:todo_index')


class TodoUpdateView(UpdateView):
    model = Todo
    template_name = "todo/update.html"
    form_class = TodoForm
    success_url = reverse_lazy('todo:todo_index')

    # def form_valid(self, form):
    #     messages.success(self.request, 'Todoを更新しました。')
    #     return redirect(self.get_success_url())
    #
    # def form_invalid(self, form):
    #     messages.error(self.request, "Todoの更新に失敗しました。")
    #     return super().form_invalid(form)


class TodoDeleteView(DeleteView):
    model = Todo
    template_name = "todo/delete.html"
    form_class = TodoForm
    success_url = reverse_lazy('todo:todo_index')

