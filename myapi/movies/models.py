from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255, null=False, blank=True)
    release_date = models.DateField(null=True)
    vote_average = models.FloatField(null=True)
    genres = models.ManyToManyField(Genre, related_name='movies')
    overview = models.TextField(null=True)
    poster_path = models.CharField(max_length=255, null=True)
    youtube_key = models.CharField(max_length=100, null=True, blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    actors = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.title