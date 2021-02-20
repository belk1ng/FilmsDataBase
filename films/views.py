from django.shortcuts import render
from .models import *
from django.views.generic import ListView


class MainPage(ListView):
    template_name = 'films/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['films'] = Film.objects.raw('SELECT * FROM films_film')  # Получаем все фильмы
        context['genres'] = Genre.objects.raw('SELECT * FROM films_genre')  # Получаем жанры (Не отображать пустые!)

        return context

    def get_queryset(self):
        return Film.objects.raw('SELECT * FROM films_film')  # Достаём данные на главную страницу



