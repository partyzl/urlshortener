from django.shortcuts import render
from .models import modelName
from .forms import formName

# Create your views here.
def index(request):
    if request.method == 'POST':
        