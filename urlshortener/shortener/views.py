from django.urls import reverse
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .forms import ShortenerForm
from .models import URL

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
            return HttpResponseRedirect(reverse("index"), context)
            return render(
                request, "index.html", context
            )  # Add the correct model stuff here
    else:
        shortener = ShortenerForm()
        recent_url = URL.objects.all().last()
        context = {
            "form": shortener,
            "shortened": f"http://localhost:8000/{recent_url.id}",
        }
        return render(request, "index.html", context)


def redirect_views(request, id):
    long_url = URL.objects.get(pk=id).long
    return redirect(long_url)
