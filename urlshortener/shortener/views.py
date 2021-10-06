from django.shortcuts import render
from .models import URL
from .forms import ShortenerForm

# Create your views here.
def index(request):

    if request.method == "POST":
        form = ShortenerForm(request.POST)
        if form.is_valid():
            context = {
                "form": ShortenerForm,
                "shortened_url": f'http://localhost:8000/{}'
            }
            return render(request, "index.html", context)

"""Need to add a way to save url here, and an else to redirect if invalid url
"""
