from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['id', 'username', 'password', 'email', 'signup_ip', 'signup_location', 'signup_holiday']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        request = self.context.get('request')

        # Ip
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        validated_data['signup_ip'] = ip

        return super().create(validated_data)
