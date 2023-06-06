from django.urls import path
from .views import register, UserDetailsView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,
)

#Routes for User
urlpatterns = [
    path('register/', register, name='register'),
    # Routes for JWT
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    # Routes for logout
    path('logout/', TokenBlacklistView.as_view(), name='token_blacklist'),

    # Routes for User Details
    path('details/',UserDetailsView.as_view(), name='user_details'),
]