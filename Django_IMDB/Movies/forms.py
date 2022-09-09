from django import forms
from . import models
from django.forms import TextInput, EmailInput


# function
class CreateReview(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['movie', 'title', 'in_long', 'score', 'user']

