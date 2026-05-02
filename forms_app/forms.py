from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ContactForm(forms.Form):
    first_name = forms.CharField(min_length=2)
    last_name = forms.CharField(required=False)
    email = forms.EmailField()
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={"placeholder": "Scrivi qui il tuo messaggio."}
        )
    )

    def clean_content(self):
        forbidden_words = ["esempio1", "esempio2"]
        data = self.cleaned_data["content"]
        content_words = data.lower().split()
        if any(word in forbidden_words for word in content_words):
            raise forms.ValidationError("Contenuto non valido!")
        return data
