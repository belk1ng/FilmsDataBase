from django.db import models
from django.urls import reverse


class Genre(models.Model):
    genre = models.CharField(max_length=50, verbose_name='Жанр', db_index=True,)

    def __str__(self):
        return self.genre

    def get_absolute_url(self):
        return reverse('genre_sort', kwargs={'genre_id': self.pk})

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['genre']


class Director(models.Model):
    director = models.CharField(max_length=50, verbose_name='Режиссёр', db_index=True)

    def __str__(self):
        return self.director

    class Meta:
        verbose_name = 'Режиссёр'
        verbose_name_plural = 'Режиссёры'
        ordering = ['director']


class Actor(models.Model):
    actor = models.CharField(max_length=50, verbose_name='Актёр', db_index=True)

    def __str__(self):
        return self.actor

    class Meta:
        verbose_name = 'Актёр'
        verbose_name_plural = 'Актёры'
        ordering = ['actor']


class Film(models.Model):
    title = models.CharField(max_length=100, verbose_name='Фильм', db_index=True,)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name='Жанр')
    directors = models.ManyToManyField(Director, verbose_name='Режиссёры')
    actors = models.ManyToManyField(Actor, verbose_name='Актёры')
    annotation = models.CharField(max_length=5000, verbose_name='Аннотация')
    awards = models.CharField(max_length=1000, verbose_name='Награды')
    release_year = models.IntegerField(verbose_name='Год релиза')
    duration = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='Продолжительность')
    url = models.URLField(max_length=500, verbose_name='Ссылка')
    image = models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name='Изображние', null=True)

    def __str__(self):
        return f'{self.title} {self.genre} {self.release_year}'

    def get_absolute_url(self):
        return reverse('get_film', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['title']



