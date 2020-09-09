#
from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from todo.models import Todo, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', )

    name = forms.CharField(label='名前', max_length=20, widget=forms.TextInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = '名前を入力してください。'
        self.fields['favorite'].widget.attrs['class'] = 'form-control'

    def __str__(self):
        return self.category


class TodoForm(forms.ModelForm):
    # デフォルトでidが付与、id=Integer, primary_key, autoincrement
    class Meta:
        model = Todo
        fields = ('title', 'description', 'due_date', 'category')

        title = forms.CharField(label='タイトル', max_length=32)
        description = forms.CharField(label='内容', max_length=32)
        due_date = forms.DateTimeField(label='期限', widget=AdminDateWidget())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs = {'class': 'form-control'}
        self.fields['description'].widget.attrs = {'class': 'form-control'}
        self.fields['category'].widget.attrs = {'class': 'form-control'}

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 6:
            raise forms.ValidationError('6文字以上です')
        return title