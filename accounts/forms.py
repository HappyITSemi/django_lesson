from accounts.models import CustomUser


class CustomSignupForm(SignupForm):
    age = forms.IntegerField()
    weight = forms.IntegerField()

    class Meta:
        model = CustomUser

    def signup(self, request,user):
        user.age = self.cleaned_data['age']
        user.weight = self.cleaned_data['weight']
        user.save()
        return user