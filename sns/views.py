import logging

from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from extra_views import InlineFormSet, InlineFormSetFactory, CreateWithInlinesView

from sns.forms import SnsForm
from sns.models import Sns
from sns_comment.forms import SnsCommentForm
from sns_comment.models import SnsComment

logger = logging.getLogger(__name__)


def add_comment(request):
    form = SnsForm(request.POST or None)
    context = {'form': form}
    # post
    # if request.method == 'POST' and form.is_valid():
    #     # sns = form.save(commit=False)
    #     # comment_formset = CommentFormset(request.POST, files=request.FILES, instance=sns)
    #     comment_formset = CommentFormset(request.POST, instance=sns)
    #     if comment_formset.is_valid().is_valid():
    #         # sns.save()
    #         comment_formset.save()
    #         return redirect('sns:sns_index')
    #     else:
    #         context['comment_formset'] = comment_formset
    # # get
    # else:
    #     # 空のformsetをテンプレートへ渡す
    #     context['comment_formset'] = CommentFormset()

    return render(request, 'sns/comment.html', context)


# 投稿の下にコメントのフォオーム
class SnsCommentInlineFormSet(InlineFormSet):
    model = SnsComment
    fields = ('comment',)
    on_delete = False


class SnsCreateInlineFormSet(CreateWithInlinesView):
    model = Sns
    fields = ('title',)
    inlines = [SnsCommentInlineFormSet, ]                   # {% for form in inlines %}
    template_name = 'sns/sns_comment_formset.html'
    success_url = 'sns:sns_index'


class SnsIndexView(ListView):
    model = Sns
    template_name = 'sns/index.html'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['me'] = self.request.user
        return context

    def get_queryset(self):
        object_list = Sns.objects.order_by('pk').all()
        # object_list = Sns.objects.filter(user=self.request.user).order_by('-sns.pk').all()
        return object_list


class SnsDetailView(DetailView):
    model = Sns
    template_name = 'sns/detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['me'] = self.request.user
        self.request.session['sns_title'] = self.object.title
        self.request.session['sns_description'] = self.object.description
        return context


class SnsCreateView(CreateView):
    model = Sns
    form_class = SnsForm
    template_name = "sns/create.html"
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
    template_name = 'sns/sns_comment_formset.html'

    def post(self, request):
        post_data = request.POST or None
        post_form = self.form_sns(post_data, prefix='post')
        comment_form = self.form_comment(post_data, prefix='sns_comment')
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



