import logging

from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from sns import forms
from sns.forms import SnsForm, SnsCommentForm
from sns.models import Sns, SnsComment

logger = logging.getLogger(__name__)


class SnsIndexView(ListView):
    model = Sns
    template_name = 'sns/index.html'
    paginate_by = 5
    logger.info('-- sns view index ---')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['me'] = self.request.user
        return context

    def get_queryset(self):
        object_list = Sns.objects.order_by('pk').all()
        # object_list = Sns.objects.filter(user=self.request.user).order_by('-sns.pk').all()
        return object_list


class SnsDetailView(DetailView, generic.edit.ModelFormMixin):
    model = Sns
    form_class = SnsForm
    logger.info('--- sns list view ---1-')
    template_name = 'sns/detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['me'] = self.request.user
        # self.post(self, request, *args, **kwargs)
        context.update({
            'sns_comment_form': forms.SnsCommentForm(**self.get_form_kwargs()),
        })
        return context

    # def post(self, request, *args, **kwargs):
    #
    #     if 'button_comment_post' in request.POST:
    #         comment_form = forms.SnsCommentForm(**self.get_form_kwargs())
    #         logger.info('--- comment_form ---1-')
    #         logger.info(comment_form)
    #         if comment_form.is_valid():
    #             comment_query = comment_form.save(commit=False)
    #             comment_query.pk = SnsComment.objects.get(pk=self.kwargs['pk'])
    #             comment_query.save()
    #             return self.form_valid(comment_form)
    #         else:
    #             # self.object = self.get_object()
    #             return self.form_invalid(comment_form)
    #     else:
    #         return


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
        sns.me = self.request.user
        sns.save()
        messages.success(self.request, 'SNSを新規作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "SNSの新規作成に失敗しました。")
        return super().form_invalid(form)


class SnsCommentView(DetailView, generic.edit.ModelFormMixin):
    # model = Sns
    fields = ()
    form_sns = SnsForm
    form_comment = SnsCommentForm
    template_name = 'sns/create_comment.html'

    def post(self, request):
        post_data = request.POST or None
        post_form = self.form_sns(post_data, prefix='post')
        comment_form = self.form_comment(post_data, prefix='comment')
        context = self.get_context_data(post_form=post_form, comment_form=comment_form)
        if post_form.is_valid():
            self.form_save(post_form)
        if comment_form.is_valid():
            self.form_save(comment_form)

        return self.render_to_response(context)

    def form_save(self, form):
        obj = form.save()
        messages.success(self.request, "{} saved successfully".format(obj))
        return obj

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        post_form = forms.SnsForm(**self.get_form_kwargs())
        comment_form = forms.SnsCommentForm(**self.get_form_kwargs())
        context.update({'post_form': post_form})
        context.update({'comment_form': comment_form})
        return self.render_to_response(context)

    def get_queryset(self):
        object_list = Sns.objects.order_by('pk').all()
        # object_list = Sns.objects.filter(user=self.request.user).order_by('-sns.pk').all()
        return object_list

    # def get_context_data(self, **kwargs):
    #     context = CreateView.get_context_data(self, **kwargs)
    #     form_comment = self.form_comment(self.request.GET or None)
    #     context.update({'form_comment': form_comment})
    #     return context


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
