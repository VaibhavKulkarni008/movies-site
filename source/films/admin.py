from django.contrib import admin

# Register your models here.
from films.models import Movie, Director, Genre

admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Genre)
