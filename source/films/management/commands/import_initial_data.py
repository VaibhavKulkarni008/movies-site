from django.core.management import BaseCommand

from films.models import Director, Genre, Movie


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        import json

        filename = "initial_data.json"

        with open(filename, 'r') as jsonfile:
            datastore = json.load(jsonfile)

            for counter,movie_data in enumerate(datastore):
                print(counter)
                director = Director.objects.create(name=movie_data["director"])

                genre_obj_list = list()
                for genre_name in movie_data["genre"]:
                    genre_name = genre_name.strip()
                    genre_obj, created = Genre.objects.get_or_create(name=genre_name)
                    genre_obj_list.append(genre_obj)

                movie = Movie.objects.create(name=movie_data["name"],
                                             imdb_score=movie_data["imdb_score"],
                                             popularity_score=movie_data["99popularity"])

                movie.directors.add(director)

                for genre_obj in genre_obj_list:
                    movie.genres.add(genre_obj)
