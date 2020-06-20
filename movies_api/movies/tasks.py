import requests
import environ

from config import celery_app
from movies_api.movies.models import Movies


env = environ.Env()

@celery_app.task()
def create_movies_database_task():
    """
        Create movies database with new movies. Returns number of
        newly created movies
    """
    THE_MOVIE_API_KEY = env("THE_MOVIE_API_KEY")
    count = 0
    for page in range(1, 11):
        resp = requests.get(
            'https://api.themoviedb.org/3/movie/now_playing?api_key='+
            THE_MOVIE_API_KEY+
            '&language=en-US&page='+
            str(page)
        )
        movies_array = []
        response_size = len(resp.json()['results'])
        tmdb_path = 'https://image.tmdb.org/t/p/w500'
        for item in resp.json()['results']:
            try:
                movie = Movies.objects.get(tmdb_id=int(item['id']))
            except Movies.DoesNotExist:
                if item['poster_path']:
                    poster_path = tmdb_path + item['poster_path']
                else:
                    poster_path = None

                movies_array.append(
                    Movies(
                        title = item['title'],
                        description = item['overview'],
                        poster_path = poster_path,
                        ranking = int(item['vote_average']),
                        tmdb_id = int(item['id']),
                    )
                )
                count += 1
        Movies.objects.bulk_create(movies_array, response_size)
    return count
