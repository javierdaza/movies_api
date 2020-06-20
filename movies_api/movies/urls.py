from django.urls import path, include

from rest_framework.routers import DefaultRouter

from movies_api.movies.api.viewsets import MoviesViewSet


router = DefaultRouter()
router.register(r'', MoviesViewSet, basename='Movies')


vote_movie_view = MoviesViewSet.as_view({'patch': 'vote_movie'})

urlpatterns = [
    path('', include(router.urls)),
    path('vote/<str:movie_id>/', vote_movie_view, name="movie_vote")
]
