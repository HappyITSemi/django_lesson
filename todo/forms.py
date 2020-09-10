#
from django import forms

from todo.models import Todo, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

    name = forms.CharField(label='名前', max_length=20)
    name.widget.attrs.update({'class': 'form-control'})

    def __str__(self):
        return self.category


class TodoForm(forms.ModelForm):
    # デフォルトでidが付与、id=Integer, primary_key, autoincrement
    class Meta:
        model = Todo
        fields = ('title', 'description', 'due_date', 'category')
        widgets = {
            'due_date': forms.SelectDateWidget(empty_label=('年', '月', '日'))
        }

        title = forms.CharField(label='タイトル', max_length=32)
        description = forms.CharField(label='内容', max_length=32)
        due_date = forms.DateTimeField(label='期限')

        title.widget.attrs.update({'class': 'form-control'})
        description.widget.attrs.update({'class': 'form-control'})

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 6:
            raise forms.ValidationError('6文字以上入力してください。')
        return title
