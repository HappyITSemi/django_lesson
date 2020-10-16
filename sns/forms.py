# sns
from django import forms

from sns.models import Sns, SnsComment


class SnsForm(forms.ModelForm):
    class Meta:
        model = Sns
        fields = ('title', 'description', 'post_image', 'me')

        title = forms.CharField(label='タイトル', max_length=32)
        description = forms.CharField(label='内容', max_length=128)  # models = TextField
        post_image = forms.ImageField(label='画像ファイル')
        widgets = {
            'post_image': forms.ClearableFileInput(attrs={
                'class': "form-control-file",
            }),
        }
        title.widget.attrs.update({'class': 'form-control'})
        description.widget.attrs.update({'class': 'form-control'})

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 6:
            raise forms.ValidationError('6文字以上入力してください。')
        return title


class SnsCommentForm(forms.ModelForm):
    class Meta:
        model = SnsComment
        fields = ('sns', 'comment')

        comment = forms.CharField(label='コメント', max_length=128)
        comment.widget.attrs.update({'class': 'form-control'})

        # def __init__(self, *args, **kwargs):
        #     # Classの指定など
        #     for field in self.fields.values():
        #         field.widget.attrs['class'] = 'form-control'

