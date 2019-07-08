from rest_framework import serializers

from .models import Director, Genre, Movie


class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = ("name", "id")


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ("name", "id")


class GetMoviesSerializer(serializers.ModelSerializer):
    directors = DirectorSerializer(many=True)
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('id', 'name', 'imdb_score', 'popularity_score',
                  'directors', 'genres')

    def to_representation(self, instance):
        data = super(GetMoviesSerializer, self).to_representation(instance)
        return data


class CreateMovieSerializer(serializers.ModelSerializer):
    directors = serializers.PrimaryKeyRelatedField(many=True, queryset=Director.objects.all())
    genres = serializers.PrimaryKeyRelatedField(many=True, queryset=Genre.objects.all())

    class Meta:
        model = Movie
        fields = ('id', 'name', 'imdb_score', 'popularity_score',
                  'directors', 'genres')
