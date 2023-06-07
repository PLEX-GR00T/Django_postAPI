from django.db import models
from django.contrib.auth import get_user_model

class Post(models.Model):
    User = get_user_model()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    liked_by = models.ManyToManyField(to=User, related_name='liked_posts', blank=True)
    
    class Meta:
        ordering = ['-created_at']



