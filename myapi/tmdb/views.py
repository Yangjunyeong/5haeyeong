from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from movies.models import Genre, Movie
import requests

# TMDB API KEY 작성
API_KEY = 'e8a979cfe459982651dedf077569ac57'

# GENRE_URL = 'https://api.themoviedb.org/3/genre/movie/list'
GENRE_URL = 'https://api.themoviedb.org/3/genre/movie/list'
# POPULAR_MOVIE_URL = 'https://api.themoviedb.org/3/movie/popular'
POPULAR_MOVIE_URL = 'https://api.themoviedb.org/3/movie/top_rated' 

def tmdb_genres():
    response = requests.get(
        GENRE_URL,
        params={
            'api_key': API_KEY,
            'language': 'ko-KR',            
        }
    ).json()    
    for genre in response.get('genres'):
        if Genre.objects.filter(pk=genre['id']).exists(): continue        
        print(genre)
        Genre.objects.create(
            id=genre['id'],
            name=genre['name']
        )
    return JsonResponse(response)


def get_youtube_key(movie_dict):    
    movie_id = movie_dict.get('id')
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}/videos',
        params={
            'api_key': API_KEY
        }
    ).json()
    for video in response.get('results'):
        if video.get('site') == 'YouTube':
            return video.get('key')
    return 'nothing'


def movie_data(page=1):
    response = requests.get(
        POPULAR_MOVIE_URL,
        params={
            'api_key': API_KEY,
            'language': 'ko-kr',     
            'page': page,       
        }
    ).json()

    for movie_dict in response.get('results'):
        if not movie_dict.get('release_date'): continue   # 없는 필드 skip
        # 유투브 key 조회

        # poster_path없다면 건너띄기
        if not movie_dict.get('poster_path'):
            continue

        youtube_key = get_youtube_key(movie_dict)

        movie = Movie.objects.create(
            id=movie_dict.get('id'),
            title=movie_dict.get('title'),
            release_date=movie_dict.get('release_date'),
            # popularity=movie_dict.get('popularity'),
            # vote_count=movie_dict.get('vote_count'),
            vote_average=movie_dict.get('vote_average'),
            overview=movie_dict.get('overview'),
            poster_path=movie_dict.get('poster_path'),   
            youtube_key=youtube_key         
        )
        for genre_id in movie_dict.get('genre_ids', []):
            movie.genres.add(genre_id)

        # 배우들 저장
        print('>>>', movie.title, '==>', movie.youtube_key)

def tmdb_data(request):
    Genre.objects.all().delete()
    Movie.objects.all().delete()

    tmdb_genres()
    for i in range(1, 50):
        movie_data(i)
    return HttpResponse('OK >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')