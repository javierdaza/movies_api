from rest_framework import viewsets, status

from rest_framework.response import Response
from .serializers import MoviesSerializer

from movies_api.movies.models import Movies


class MoviesViewSet(viewsets.ModelViewSet):
    """
    Endpoints for movies. Also there is an enpoint for voting movies
    """
    serializer_class = MoviesSerializer
    queryset = Movies.objects.all()

    def vote_movie(self, request, movie_id):
        try:
            if not request.data['ranking'] or type(request.data['ranking']) != int:
                return Response(
                    'Your vote cannot be empty or not an integer',
                    status=status.HTTP_400_BAD_REQUEST
                )
            movie = Movies.objects.get(id=movie_id)
            new_avg = (movie.ranking + request.data['ranking']) // 2
            movie.ranking = new_avg
            movie.save()
            serializer = MoviesSerializer(movie)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Movies.DoesNotExist:
            return Response('Movie not found', status=status.HTTP_404_NOT_FOUND)
