from django.db import models
from django.conf import settings
from movies.models import Movie

class Comment(models.Model):
    STAR_CHOICES = [
        (1, '1점'),
        (2, '2점'),
        (3, '3점'),
        (4, '4점'),
        (5, '5점'),
    ]

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_comments')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(null=False)
    star = models.IntegerField(choices=STAR_CHOICES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content