from django.shortcuts import render
from .models import *
from django.views.generic import ListView


def index(request):  # Главная страница
    genres = Genre.objects.raw("SELECT * FROM films_genre")
    films = Film.objects.raw("SELECT * FROM films_film")

    return render(request, "films/index.html", {"genres": genres, "films": films})

