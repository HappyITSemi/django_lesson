# sns
from django import forms
from sns_comment.models import SnsComment


class SnsCommentForm(forms.ModelForm):
    class Meta:
        model = SnsComment
        fields = ('me', 'comment')

        comment = forms.CharField(label='コメント', max_length=128)
        comment.widget.attrs.update({'class': 'form-control'})

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 6:
            raise forms.ValidationError('6文字以上入力してください。')
        return title
