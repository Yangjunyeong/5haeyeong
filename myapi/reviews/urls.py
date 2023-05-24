from django.urls import path
from reviews.views import create_review, get_reviews

app_name = 'reviews'

urlpatterns = [
    path('reviews/<int:movie_id>/create/', create_review, name='create_review'),
    path('reviews/<int:movie_id>/', get_reviews, name='get_reviews'),
]