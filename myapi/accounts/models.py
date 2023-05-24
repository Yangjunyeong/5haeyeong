from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Genre

class User(AbstractUser):
    selectedGenres = models.ManyToManyField(Genre, blank=True)