from django import forms
from .models import User


class SignupForm(forms.ModelForm):

    class Meta:
        model = User

        fields = [
            "username",
            "email",
            "password",
            "user_type",
            "profile_pic"
        ]

    def clean_email(self):

        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "Email already exists"
            )

        return email


class LoginForm(forms.Form):

    email = forms.EmailField()

    password = forms.CharField()