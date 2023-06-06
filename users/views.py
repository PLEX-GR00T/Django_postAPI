# from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
# from rest_framework_simplejwt.views import TokenBlacklistView
# from rest_framework.views import APIView
# from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
@api_view(['POST'])
def register(request):
    # # Ip
    # x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    # if x_forwarded_for:
    #     ip = x_forwarded_for.split(',')[0]
    # else:
    #     ip = request.META.get('REMOTE_ADDR')

    serializer:UserSerializer = UserSerializer(data=request.data, context = {'request': request})

    if serializer.is_valid():
        # serializer.validated_data['signup_ip'] = ip
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()
        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        },status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailsView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user





















# # We need to crate logout view to blacklist the refresh token
# class LogoutView(TokenBlacklistView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         try:
#             token = RefreshToken(request.data["refresh_token"])
#             token.blacklist()
#             return Response(data={"success": "Successfully logged out."}, status=200)
#         except Exception as e:
#             return Response(data={"error": str(e)}, status=400)