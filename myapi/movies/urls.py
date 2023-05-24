from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    # 영화 기본 기능
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('movies/genres/', views.genres_list, name='genres_list'),
    

    # path('add_movie_info/<int:movie_pk>/', views.add_movie_info),
    # path('<int:movie_pk>/like/', views.movie_like),
    # path('search/<query>/', views.movie_search),
    # tmdb api
    # path('tmdb/', views.tmdb_movie),
]