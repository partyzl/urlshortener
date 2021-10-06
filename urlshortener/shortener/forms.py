from django import forms
from . import models


class ShortenerForm(forms.ModelForm):
    class Meta:
        model = models.URL
        fields = ["long"]

    def __init__(self, *args, **kwargs):
        super(ShortenerForm, self).__init__(*args, **kwargs)
        self.fields["long"].label = "What you wanna shorten?"
