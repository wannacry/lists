from django.db import models
from django.db.models import CharField



class MovieGenres(models.Model):

    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    imdb_id = models.CharField(max_length=20,blank=True,null=True)
    genres = models.ManyToManyField(MovieGenres)
    title = models.CharField(max_length=255)
    overview = models.TextField(blank=True, null=True)
    poster_path = models.CharField(max_length=255, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    revenue = models.PositiveBigIntegerField(blank=True, null=True)
    budget = models.PositiveBigIntegerField(blank=True, null=True)
    runtime = models.PositiveBigIntegerField(blank=True, null=True)
    imdb_rating = models.FloatField(blank=True,null=True)
    vote_average = models.FloatField(blank=True,null=True)
    vote_count = models.PositiveIntegerField(blank=True,null=True)
    status = CharField(max_length=50)
    popularity = models.FloatField(blank=True,null=True)

    def __str__(self):
        return self.title


class Country(models.Model):
    iso_3166_1 = models.CharField(max_length=2, primary_key=True)
    english_name = models.CharField(max_length=100)
    native_name = models.CharField(max_length=100)

    def __str__(self):
        return self.english_name

class Language(models.Model):
    iso_639_1 = models.CharField(max_length=2, primary_key=True)
    english_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.english_name

