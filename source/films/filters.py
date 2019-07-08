import django_filters

from .models import Movie


class MovieFilter(django_filters.FilterSet):

    directors = django_filters.CharFilter(method='filter_by_directors')
    genres = django_filters.CharFilter(method='filter_by_genres')

    class Meta:
        model = Movie
        fields = ('imdb_score', 'popularity_score', 'directors', 'genres')

    def filter_by_directors(self, queryset, name, value):
        queryset = queryset.filter(directors__id__in=[int(_) for _ in value.split(',')])
        return queryset.distinct()

    def filter_by_genres(self, queryset, name, value):
        queryset = queryset.filter(genres__id__in=[int(_) for _ in value.split(',')])
        return queryset.distinct()
