import logging

from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from sns.forms import SnsForm
from sns.models import Sns

logger = logging.getLogger(__name__)


# @login_required
class SnsIndexView(ListView):
    model = Sns
    template_name = 'sns/index.html'
    paginate_by = 3
    logger.info('-- sns view index ---')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        # context['me'] =
        # context['friends'] =
        logger.info('-- sns index get_context_data ---')
        return context


def get_queryset(self):
    object_list = Sns.objects.filter(user=self.request.user).order_by('sns.id').all()
    return object_list


class SnsDetailView(DetailView):
    model = Sns
    form_class = SnsForm
    template_name = 'sns/detail.html'


class SnsCreateView(CreateView):
    model = Sns
    form_class = SnsForm
    template_name = "sns/create.html"
    logger.info('--- sns create view ---1-')
    success_url = reverse_lazy('sns:sns_index')

    def form_valid(self, form):
        sns = form.save(commit=False)
        sns.user = self.request.user  # Login-userをセットする
        logger.info('--- sns create view ---2-')
        logger.info(self.request.user)
        sns.save()
        messages.success(self.request, 'SNSを新規作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "SNSの新規作成に失敗しました。")
        return super().form_invalid(form)


class SnsUpdateView(UpdateView):
    model = Sns
    form_class = SnsForm
    template_name = "sns/update.html"
    success_url = reverse_lazy('sns:sns_index')

    def get_success_url(self):
        return reverse_lazy('sns:sns_detail', kwargs={'pk': self.kwargs['pk']})


class SnsDeleteView(DeleteView):
    model = Sns
    form_class = SnsForm
    template_name = "sns/delete.html"
    success_url = reverse_lazy('sns:sns_index')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "SNSを削除しました。")
        return super().delete(request, *args, **kwargs)
