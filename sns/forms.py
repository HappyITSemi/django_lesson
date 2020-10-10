# sns
from django import forms

from sns.models import Mention


class MentionForm(forms.ModelForm):
    class Meta:
        model = Mention
        fields = ('me', 'title', 'description')

