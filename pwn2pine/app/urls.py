# app/urls.py

from django.urls import path
from app import views

urlpatterns = [
    path("", views.index, name='index'),
    path("<int:id>", views.index, name='index'),
    path("jsonp", views.callback, name='callback'),
]
