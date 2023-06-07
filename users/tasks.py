import requests
import json
from datetime import datetime
from django.contrib.auth import get_user_model
from time import sleep

def enrich_user_data(user_id):
    # sleep(30)
    User = get_user_model()
    user = User.objects.get(id = user_id)

    # Geo location (Todo: Handle API exceptions, move keys to env file,)
    response = json.loads(requests.get(f"https://ipgeolocation.abstractapi.com/v1/?api_key=fcc203c58fa14456839d1646a45107b8&ip_address={user.signup_ip}").content)
    user.signup_location = f"{response['city']};{response['region']};{response['country']}"
    user.save()

    # Time Zone
    timezone = json.loads(requests.get(f'https://timezone.abstractapi.com/v1/current_time/?api_key=c053f763e49a4f59be1810a1f73322de&location="{user.signup_ip}"').content)
    # print(timezone)
    dt = datetime.fromisoformat(timezone['datetime'])
    
    # Is holiday
    holiday = json.loads(requests.get(f"https://holidays.abstractapi.com/v1/?api_key=f688711adcb44155ae10450710577340\
                                        &country={response['country_code']}&year={dt.year}&month={dt.month}&day={dt.day}").content)

    if holiday:
        for h in holiday:
            if h["type"] in ['public_holiday', 'religious_holiday','National']:
                user.signup_holiday = True
                break
    else:
        user.signup_holiday = False
    user.save()