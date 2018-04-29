from django import forms
from django.core import validators
from . import models

def must_be_empty(value):
    if value:
        raise forms.ValidationError('is not empty')

class DiscussionForm(forms.ModelForm):
    class Meta:
        model = models.Discussion
        fields = [
                  'name',
                  'email',
                  'subject',
                  'discussion',
        ]

class BrowseDissForm(forms.ModelForm):
    class Meta:
        model = models.Discussion
        fields = [
                  'name',
                  'email',
                  'subject',
                  'discussion',
                  'datecreated',
        ]
