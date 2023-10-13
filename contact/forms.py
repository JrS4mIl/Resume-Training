from django import forms
from django.core.mail import EmailMessage
from django.conf import settings


class ContactForm(forms.Form):
    name = forms.CharField(max_length=120, required=True)
    email = forms.EmailField(max_length=120, required=True)
    subject = forms.CharField(max_length=120, required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)

