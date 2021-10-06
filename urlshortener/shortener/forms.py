from django import forms
from . import models


class ShortenerForm(forms.ModelForm):

    class Meta:
        model = models.URL
        fields = ['long']
