from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('cs50/', views.cs50_links, name='cs50_links'),
]
