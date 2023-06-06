from rest_framework import serializers
from .models import User
import requests
import json
from datetime import datetime

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

        # Geo location (Todo: Handle API exceptions)
        response = json.loads(requests.get(f"https://ipgeolocation.abstractapi.com/v1/?api_key=fcc203c58fa14456839d1646a45107b8&ip_address={ip}").content)
        validated_data['signup_location'] = f"{response['city']};{response['region']};{response['country']}"

        # Time Zone
        timezone = json.loads(requests.get(f'https://timezone.abstractapi.com/v1/current_time/?api_key=2f0631b8bdcf41ff90277c285f120622&location="{ip}"').content)
        dt = datetime.fromisoformat(timezone['datetime'])
        
        # Is holiday
        holiday = json.loads(requests.get(f"https://holidays.abstractapi.com/v1/?api_key=f688711adcb44155ae10450710577340\
                                          &country={response['country_code']}&year={dt.year}&month={dt.month}&day={dt.day}").content)
   
        if holiday:
            for h in holiday:
                if h["type"] in ['public_holiday', 'religious_holiday','National']:
                    validated_data['signup_holiday'] = True
                    break
        else:
            validated_data['signup_holiday'] = False

        return super().create(validated_data)
