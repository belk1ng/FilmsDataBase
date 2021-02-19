from django.contrib import admin
from .models import Genre, Actor, Director, Film


class GenreAdmin(admin.ModelAdmin):
    list_display = ['genre']
    list_display_links = ['genre']
    search_fields = ['genre']


class ActorAdmin(admin.ModelAdmin):
    list_display = ['actor']
    list_display_links = ['actor']
    search_fields = ['actor']


class DirectorAdmin(admin.ModelAdmin):
    list_display = ['director']
    list_display_links = ['director']
    search_fields = ['director']


class FilmAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'annotation',
                    'awards', 'release_year', 'duration', 'url']
    list_display_links = ['title', 'url']
    search_fields = ['title', 'genre', 'directors', 'actors', 'release_year']


admin.site.register(Genre, GenreAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Film, FilmAdmin)

