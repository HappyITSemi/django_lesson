#
from django import forms

from article.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'description', 'post_image', 'me', 'likes')

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

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 6:
            raise forms.ValidationError('6文字以上入力してください。')
        return description

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        description = cleaned_data.get('description')
        if not (title or description):
            raise forms.ValidationError("タイトルと記事を入力して下さい")
        return cleaned_data
