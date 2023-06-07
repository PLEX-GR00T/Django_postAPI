from django.urls import path
from .views import PostListCreateView, PostRUDView


#Routes for User
urlpatterns = [
    path('', PostListCreateView.as_view(), name='posts_list_create'),
    path('<int:pk>/', PostRUDView.as_view(), name='posts_rud'),
   
]