from django import forms
from django.forms import TextInput, Textarea, EmailInput
from django.utils.translation import gettext_lazy as _

from . models import HireMessage


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = HireMessage
        # exclude = ('auto_id')
        fields = ['name', 'email', 'subject', 'company', 'message',]
        widgets = {
            'name': TextInput(attrs={'class': 'form-group form-control', 'placeholder': "May I know your name?",
                                     'required': True}),
            'email': EmailInput(attrs={'class': 'form-group form-control', 'placeholder': "Can I get your email address?",
                                       'required': True}),
            'subject': TextInput(attrs={'class': 'form-group form-control', 'placeholder': "May I ask what it is regarding?",
                                        'required': True}),
            'company': TextInput(
                attrs={'class': 'form-group form-control', 'placeholder': "May I ask your organization name?",
                       'required': True}),
            'message': Textarea(attrs={'class': 'form-group form-control', 'placeholder': 'Please write your message...',
                                       'required': True}),
        }
        error_messages = {
            'name': {
                'required': _("Your name is required"),
            },
            'email': {
                'required': _("Valid email is required"),
            },
            'subject': {
                'required': _("Subject is required"),
            },
            'company': {
                'required': _("Company is required"),
            },
            'message': {
                'required': _("Message cannot be empty"),
            },
        }
        labels = {
            "name": "May I know your name?",
            "email": "Can I get your email address?",
            "subject": "May I ask what it is regarding?",
            "company": "May I ask your organization name?",
            "message": "Please write your message...",
        }
