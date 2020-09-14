#
import logging

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView, TemplateView

from todo.forms import TodoForm
from todo.models import Todo, Category

logger = logging.getLogger(__name__)


class TodoIndexView(ListView):
    model = Todo
    template_name = 'todo/index.html'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.order_by('pk').all()
        return context

    def get_queryset(self):
        print(self.request.user.id)
        print(self.request.user)
        object_list = Todo.objects.filter(user=self.request.user).order_by('todo.id').all()
        return object_list


class TodoDetailView(DetailView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo/detail.html'


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    form_class = TodoForm
    template_name = "todo/create.html"
    success_url = reverse_lazy('todo:todo_index')

    def form_valid(self, form):
        todo = form.save(commit=False)
        todo.user = self.request.user
        print(self.request.user)
        todo.save()
        messages.success(self.request, 'Todoを作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Todoの作成に失敗しました。")
        return super().form_invalid(form)


class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = "todo/update.html"
    success_url = reverse_lazy('todo:todo_index')


class TodoDeleteView(DeleteView):
    model = Todo
    form_class = TodoForm
    template_name = "todo/delete.html"
    success_url = reverse_lazy('todo:todo_index')

    def post(self, request, *args, **kwargs):
        user = self.request.user
