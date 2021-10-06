from django import forms
from .models import URL


class ShortenerForm(forms.ModelForm):
    new_url = forms.CharField(label="Enter URL Here", max_length=200)
