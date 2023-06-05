from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['id', 'username', 'password', 'email', 'signup_ip', 'signup_location', 'signup_holiday']
        extra_kwargs = {'password': {'write_only': True}}