from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.
class User(AbstractUser):
    signup_ip = models.CharField(max_length=255, null=True, blank=True) 
    signup_location = models.CharField(max_length=255, null=True, blank=True)
    signup_holiday = models.BooleanField(default=False)