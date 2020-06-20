import requests
import environ

from config import celery_app
from movies_api.movies.models import Movies


env = environ.Env()

@celery_app.task()
def create_movies_database_task():
    """Create movies database with new movies."""
    THE_MOVIE_API_KEY = env("THE_MOVIE_API_KEY")
    resp = requests.get(
        'https://api.themoviedb.org/3/movie/now_playing?api_key='+
        THE_MOVIE_API_KEY+
        '&language=en-US&page=1'
    )
    movies_array = []
    response_size = len(resp.json()['results'])
    for item in resp.json()['results']:
        # TODO: Check if movie already exists
        movies_array.append(
            Movies(
                title = item['title'],
                description = item['overview'],
                poster_path = item['poster_path'],
                ranking = int(item['vote_average']),
            )
        )
    Movies.objects.bulk_create(movies_array, response_size)
    return resp.status_code
