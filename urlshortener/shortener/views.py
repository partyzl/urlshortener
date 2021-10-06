from django.urls import reverse
from django.shortcuts import redirect, render, get_object_or_404
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
                "form": shortener
                # "shortened": f"http://localhost:8000/{url.id}",
            }
            return HttpResponseRedirect(f'{reverse("index-uid")}?uid={url.id}', context)
            # return render(
            #     request, "index.html", context
            # )  # Add the correct model stuff here
    else:
        shortener = ShortenerForm()
        context = {
            "form": shortener
        }
        return render(request, "index.html", context)

def index_uid(request):
        uid = request.GET.get('uid')
        # recent_url = URL.objects.all().last()
        # recent_url = URL.object.get(pk=uid)
        recent_url = get_object_or_404(URL, pk=uid)
        context = {
            "shortened": f"http://localhost:8000/{recent_url.id}",
            "uid": True
        }
        return render(request, "index.html", context)



def redirect_views(request, id):
    long_url = URL.objects.get(pk=id).long
    print(long_url)
    return redirect(long_url)
