from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import  Genre, Movie


# MovieSerializer
# poster_path, title, vote_average, actors, genres, overview

class GenreListSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Genre
        fields = '__all__'
        # fields = ('id', 'title', 'content', 'user', 'username')

class MovieDetailSerializer(serializers.ModelSerializer):



    class GenreListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = '__all__'

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id',) 

    
    genres = GenreListSerializer(many=True, read_only=True)
    like_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = (
            'id', 'poster_path', 'title', 'vote_average', 'actors', 'genres', 'overview', 'like_users',
            )
        read_only_fields = ('actors', 'genres', )
    


# poster_path, title, release_date, vote_average
class MovieListSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'nickname',)

    like_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path', 'like_users', 'vote_average',)
        read_only_fields = ('like_users',)