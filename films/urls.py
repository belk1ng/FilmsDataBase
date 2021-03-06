from django.urls import path
from .views import MainPage, GetFilm, SortByGenre, SearchFilms


urlpatterns = [
    path('', MainPage.as_view(), name='home'),
    path('get_film/<int:pk>/', GetFilm.as_view(), name='get_film'),
    path('sort_by_genre/<int:genre_id>/', SortByGenre.as_view(), name='genre_sort'),
    path('search/', SearchFilms.as_view(), name='search_films'),
]
