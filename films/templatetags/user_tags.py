from django import template
from films.models import *

register = template.Library()  # Регаем теги


@register.inclusion_tag('films/render_genres.html')
def render_genres():
	return {'genres': Genre.objects.raw('''SELECT g.id, COUNT(title), genre FROM films_film AS f 
		INNER JOIN films_genre AS g ON f.genre_id = g.id 
		GROUP BY g.id, genre HAVING COUNT(title) > 0''')
	}  # Возвращаем непустые жанры

