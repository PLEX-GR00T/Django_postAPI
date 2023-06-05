from django.urls import path
from .views import register

#Routes for User
urlpatterns= [path('register/', register, name='register'),]