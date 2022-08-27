from django import forms
from . import models


class CreateReview(forms.ModelForm):
    class Meta:
        model = models.Movie
        fields = ['title', 'plot', 'cast', 'slug']
