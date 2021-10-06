from django.shortcuts import render
from . import models
from .forms import ShortenerForm

# Create your views here.
def index(request):
    if request.method == "POST":
        form = ShortenerForm(request.POST)
        if form.is_valid():
            return render(request, 'index.html')
    return render(request, 'index.html')


"""Need to add a way to save url here, and an else to redirect if invalid url
"""
