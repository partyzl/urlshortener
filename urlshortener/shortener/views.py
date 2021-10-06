from django.shortcuts import render
from .forms import ShortenerForm

# Create your views here.
def index(request):
    if request.method == "POST":
        given_url = ShortenerForm(request.POST)
        if given_url.is_valid():
            url = given_url.save()
            shortener = ShortenerForm()
            context = {
                "form": shortener,
                "shortened": f"http://localhost:8000/{url.id}",
            }
            return render(
                request, "index.html", context
            )  # Add the correct model stuff here
    else:
        shortener = ShortenerForm()
        context = {"form": shortener, "shortened": "This aint a valid ting"}
        return render(request, "index.html", context)


"""Need to add a way to print url to page here
"""
