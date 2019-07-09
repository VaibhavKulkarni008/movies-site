from django.shortcuts import render

# Create your views here.
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from django_filters import rest_framework as django_filters

from common.permissions import IsAdminOrReadOnly
from .filters import MovieFilter
from .models import Movie, Director
from .serializers import GetMoviesSerializer, CreateMovieSerializer, DirectorSerializer, GenreSerializer
from common.paginations import ThirtyPagePagination


class MoviesViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, django_filters.DjangoFilterBackend)
    filter_class = MovieFilter
    pagination_class = ThirtyPagePagination
    search_fields = ('name', )
    ordering_fields = ('name', 'imdb_score', 'popularity_score')
    permission_classes = (IsAdminOrReadOnly,)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return GetMoviesSerializer
        else:
            return CreateMovieSerializer


class DirectorViewSet(ModelViewSet):
    queryset = Director.objects.all()
    pagination_class = ThirtyPagePagination
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = DirectorSerializer


class GenreViewSet(ModelViewSet):
    queryset = Director.objects.all()
    pagination_class = ThirtyPagePagination
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = GenreSerializer
