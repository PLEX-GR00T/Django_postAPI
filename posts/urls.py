from django.urls import path
from .views import PostListCreateView, PostRUDView, PostLikeUnlikeView


#Routes for User
urlpatterns = [
    path('', PostListCreateView.as_view(), name='posts_list_create'),
    path('<int:pk>/', PostRUDView.as_view(), name='posts_rud'),
    path('<int:pk>/like-toggle/', PostLikeUnlikeView.as_view(), name='posts_like_unlike'),
]