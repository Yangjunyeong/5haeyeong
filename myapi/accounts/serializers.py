from rest_framework import serializers
from django.contrib.auth import get_user, get_user_model
from .models import User
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = '__all__'

