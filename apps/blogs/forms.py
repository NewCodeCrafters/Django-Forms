from django import forms
from .models import Blogs

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blogs

        fields = [
            "Title",
            "description"
            "image",
            "status"
        ]

        def clean_title(self):
            title = self.clean_title.get("title")

            if len(title) < 5:
                raise forms.ValidationError(
                    "Title must contain at least 5 characters."
                )
            return title
        
        def clean_description(self):
            description = self.cleaned_data.get("description")

            if len(description) < 20:
                raise forms.ValidationError(
                    "Description must be descriptive."
                )
            return description