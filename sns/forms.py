# sns
from django import forms

from sns.models import Sns


class SnsForm(forms.ModelForm):  # mentiionForm
    class Meta:
        model = Sns
        fields = ('me', 'title', 'description')
