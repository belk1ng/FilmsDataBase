from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class MainPage(ListView):
    template_name = 'films/index.html'
    context_object_name = 'films'
    paginate_by = 2

    def get_queryset(self):
        films = Film.objects.raw('SELECT * FROM films_film ORDER BY id DESC')  # Достаём данные на главную страницу

        return films




class SortByGenre(ListView):  # Страница для фильмов с сортировкой по жанру
    template_name = 'films/sort_by_genre.html'
    context_object_name = 'films'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(SortByGenre, self).get_context_data(**kwargs)
        context['cur_genre'] = Genre.objects.get(pk=self.kwargs['genre_id'])

        return context

    def get_queryset(self):  # Достаём сортированные по жанру фильмы
            return Film.objects.raw('''SELECT * FROM films_film
                                    WHERE genre_id = {} ORDER BY id DESC
                                    '''.format(self.kwargs['genre_id']))


class GetFilm(DetailView):  # Подробная страница для фильма
    model = Film
    template_name = 'films/get_film.html'
    context_object_name = 'film'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super(GetFilm, self).get_context_data(**kwargs)
        context['actors'] = Actor.objects.raw('''SELECT f.id, actor FROM films_film_actors AS fa
                                                INNER JOIN films_film AS f ON fa.film_id = f.id
                                                INNER JOIN films_actor AS a ON fa.actor_id = a.id
                                                WHERE f.id = {}
                                                '''.format(self.kwargs['pk']))  # Достаём актёров к фильму по его айди

        context['directors'] = Film.objects.raw('''SELECT f.id, director FROM films_film_directors AS fd
                                                INNER JOIN films_film AS f ON fd.film_id = f.id
                                                INNER JOIN films_director AS d ON fd.director_id = d.id
                                                WHERE f.id = {}
                                                '''.format(self.kwargs['pk'])) # Достаём режиссёров к фильму по айди
        return context


class SearchFilms(ListView):
    context_object_name = 'films'
    template_name = 'films/search.html'

    def get_context_data(self, **kwargs):
        context = super(SearchFilms, self).get_context_data(**kwargs)
        context['header'] = self.request.GET.get('films_search')

        return context

    def get_queryset(self):
        query = self.request.GET.get('films_search')  # Получаем запрос из формы

        return Film.objects.filter(Q(title__icontains=query) |
                                    Q(genre__genre__icontains=query) |
                                    Q(annotation__icontains=query) |
                                    Q(actors__actor__icontains=query)|
                                    Q(directors__director__icontains=query) |
                                    Q(release_year__icontains=query)
                                    ).distinct()  # Получаем данные по запросу с помощью ORM (sql-запрос очень сложный, поэтому упрощаем задачу)




