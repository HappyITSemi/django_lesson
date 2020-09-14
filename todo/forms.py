#
from django import forms

from todo.models import Todo, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

    name = forms.CharField(label='名前', max_length=32)
    name.widget.attrs.update({'class': 'form-control'})

    def __str__(self):
        return self.category


class TodoForm(forms.ModelForm):
    # デフォルトでidが付与、id=Integer, primary_key, autoincrement
    class Meta:
        model = Todo
        fields = ('name', 'description', 'due_date', 'category')
        widgets = {
            'due_date': forms.SelectDateWidget(empty_label=('年', '月', '日'))
        }

        name = forms.CharField(label='タイトル', max_length=32)
        description = forms.CharField(label='内容', max_length=32)
        due_date = forms.DateTimeField(label='期限')

        name.widget.attrs.update({'class': 'form-control'})
        description.widget.attrs.update({'class': 'form-control'})
        due_date.widget.attrs.update({'class': 'form-control'})

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 6:
            raise forms.ValidationError('6文字以上入力してください。')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 1:
            raise forms.ValidationError('内容を入力してください。')
        return description

    # def clean_due_date(self):
    #     due_date = self.cleaned_data.get('description')
    #     if (not due_date.year) or (not due_date.month) or (not due_date.day):
    #         raise forms.ValidationError('年月日を入力してください。')
    #     return due_date
