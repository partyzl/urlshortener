from django.shortcuts import redirect
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>", views.redirect_views),
    path("uid/", views.index_uid, name="index-uid")
]
