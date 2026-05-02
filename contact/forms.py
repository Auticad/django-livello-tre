from django import forms

from contact.models import ContactMessage


class ContactMessageModelForm(forms.ModelForm):
    
    class Meta:
        model = ContactMessage
        fields = "__all__"