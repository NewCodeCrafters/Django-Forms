from django import forms
from .models import User

class SignupForm(forms.ModelForm):

    class Meta:
        model = User

        fields = [
            "username",
            'email',
            'password',
            "user_type",
            "profile_pic"
        ]

        def clean(self):
            email = self.cleaned_data.get("email")

            if User.objects.filter(email=email).exists():
                raise forms.ValidationError(
                    "Email or User already exists"
                )
            

class Loginform(forms.ModelForm):

    class Meta:
        model = User

        fields = [
            "email",
            "password"
        ]