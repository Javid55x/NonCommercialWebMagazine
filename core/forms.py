from dataclasses import fields
from django import forms
from .models import Contact
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'contact-form-txt',
        'placeholder':_('Ad')
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'contact-form-txt',
        'placeholder':_('Email')
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class':'contact-form-textarea',
        'placeholder':_('Mətin')
    }))

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
