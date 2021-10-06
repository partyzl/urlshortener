from django.shortcuts import redirect
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatters = [path("", views.index, name="index")]
