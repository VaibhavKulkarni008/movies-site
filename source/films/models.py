from django.db import models

# Create your models here.
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Director(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(unique=True, max_length=30)

    def __str__(self):
        return self.name


class Movie(models.Model):

    name = models.CharField(max_length=30)

    imdb_score = models.DecimalField(max_digits=3,
                                     decimal_places=1,
                                     validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])

    popularity_score = models.DecimalField(max_digits=5,
                                           decimal_places=2,
                                           validators=[MinValueValidator(0.00), MaxValueValidator(100.00)])

    directors = models.ManyToManyField('Director', related_name='movies', verbose_name='directed by')

    genres = models.ManyToManyField('Genre', related_name='movies')

    def __str__(self):
        return self.name
