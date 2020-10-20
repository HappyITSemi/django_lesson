import logging

from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from sns_comment.forms import SnsCommentForm
from sns_comment.models import SnsComment

logger = logging.getLogger(__name__)


class SnsCommentIndexView(ListView):
    model = SnsComment
    template_name = 'sns_comment/index.html'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        #
        return context

    def get_queryset(self):
        object_list = SnsComment.objects.order_by('pk').all()
        # object_list = Sns.objects.filter(user=self.request.user).order_by('-sns.pk').all()
        return object_list


class SnsCommentDetailView(DetailView):
    model = SnsComment
    template_name = 'sns_comment/detail.html'


class SnsCommentCreateView(CreateView):
    model = SnsComment
    form_class = SnsCommentForm
    template_name = "sns_comment/create.html"
    success_url = reverse_lazy('sns_comment:sns_comment_index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['me'] = self.request.user

        # if 'key' in request.session
        context['sns_title'] = self.request.session['sns_title']  # get session data
        context['sns_description'] = self.request.session['sns_description']
        del self.request.session['sns_title']
        del self.request.session['sns_description']
        return context

    def form_valid(self, form):
        sns_comment = form.save(commit=False)
        sns_comment.user = self.request.user

        sns_comment.me = self.request.user
        sns_comment.save()
        messages.success(self.request, 'SNS_Commentを新規作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "SNSコメントの新規作成に失敗しました。")
        return super().form_invalid(form)


class SnsCommentUpdateView(UpdateView):
    model = SnsComment
    form_class = SnsCommentForm
    template_name = "sns_comment/update.html"
    success_url = reverse_lazy('sns_comment:sns_comment_index')

    def get_success_url(self):
        return reverse_lazy('sns_comment:sns_comment_detail', kwargs={'pk': self.kwargs['pk']})


class SnsCommentDeleteView(DeleteView):
    model = SnsComment
    form_class = SnsCommentForm
    template_name = "sns_comment/delete.html"
    success_url = reverse_lazy('sns_comment:sns_comment_index')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "SNSコメントを削除しました。")
        return super().delete(request, *args, **kwargs)
