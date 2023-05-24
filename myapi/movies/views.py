from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Movie, Genre
from .serializers import MovieListSerializer, MovieDetailSerializer, GenreListSerializer
import requests
from django.conf import settings

@api_view(['GET', 'DELETE', 'PUT'])
def movie_detail(request, movie_id):
    # article = Article.objects.get(pk=article_pk)
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.method == 'GET':
        serializer = MovieDetailSerializer(movie)
        print(serializer.data)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = MovieDetailSerializer(movie, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def movie_list(request):
    if request.method == 'GET':

        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MovieDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        


# TMDB API 키
API_KEY = 'e8a979cfe459982651dedf077569ac57'

# Django 서버 URL
SERVER_URL = 'http://127.0.0.1:8000/'

# TMDB에서 영화 데이터 가져오기
def fetch_movies():
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        movies = response.json().get('results')
        return movies
    else:
        print('Error fetching movies:', response.status_code)
        return None

# 장르 정보 가져오기
def get_genre(genre_ids):
    genres = Genre.objects.filter(id__in=genre_ids)
    return genres

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def genres_list(request):
    if request.method == 'GET':
        # genress = genres.objects.all()
        genres = get_list_or_404(Genre)
        serializer = GenreListSerializer(genres, many=True)
        return Response(serializer.data)


# 영화 데이터를 Django 서버에 저장하기
def save_movies_to_server(movies):
    for movie in movies:
        # 장르 정보 가져오기
        genre_ids = movie['genre_ids']
        genres = get_genre(genre_ids)

        # Movie 모델에 데이터 저장
        movie_obj = Movie()
        movie_obj.title = movie['title']
        movie_obj.release_date = movie['release_date']
        movie_obj.vote_average = movie['vote_average']
        movie_obj.overview = movie['overview']
        # 필요한 영화 정보를 추가로 입력하세요

        # ManyToMany 필드에 장르 추가
        movie_obj.save()
        movie_obj.genres.set(genres)

        print(f'Movie "{movie["title"]}" saved to server.')


# 메인 함수: 영화 데이터 가져오기 및 서버에 저장하기
def main():
    movies = fetch_movies()
    if movies:
        save_movies_to_server(movies)

main()