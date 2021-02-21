from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView
from django.http import Http404


class MainPage(ListView):
    template_name = 'films/index.html'

    def get_context_data(self, **kwargs):
        context = super(MainPage, self).get_context_data(**kwargs)
        context['films'] = Film.objects.raw('SELECT * FROM films_film')  # Получаем все фильмы

        return context

    def get_queryset(self):  
        return Film.objects.raw('SELECT * FROM films_film')  # Достаём данные на главную страницу


class SortByGenre(ListView):  # Страница для фильмов с сортировкой по жанру
	template_name = 'films/sort_by_genre.html'
	context_object_name = 'films'

	def get_queryset(self):  # Достаём сортированные по жанру фильмы
		return Film.objects.raw('SELECT * FROM films_film WHERE genre_id = {}'.format(self.kwargs['genre_id']))


class GetFilm(DetailView):  # Подробная страница для фильма
	model = Film
	template_name = 'films/get_film.html'
	context_object_name = 'film'
	pk_url_kwarg = 'pk'

	def get_context_data(self, **kwargs):
	    context = super(GetFilm, self).get_context_data(**kwargs)
	    context['actors'] = Film.objects.raw('''
	    			SELECT f.id, actor FROM films_film_actors AS fa
					INNER JOIN films_film AS f ON fa.film_id = f.id
					INNER JOIN films_actor AS a ON fa.actor_id = a.id
					WHERE f.id = {}
	    			'''.format(self.kwargs['pk']))  # Достаём актёров к фильму по его айди
	    
	    context['directors'] = Film.objects.raw('''
	    			SELECT f.id, director FROM films_film_directors AS fd
					INNER JOIN films_film AS f ON fd.film_id = f.id
					INNER JOIN films_director AS d ON fd.director_id = d.id
					WHERE f.id = {}
	    			'''.format(self.kwargs['pk'])) # Достаём режиссёров к фильму по айди

	    return context

