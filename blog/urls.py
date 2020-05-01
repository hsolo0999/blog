from django.urls import path
from django.shortcuts import redirect
from .views import ShowPosts, PostCreate

urlpatterns = [
    path('', lambda request: redirect('show_posts/', permanent=False)),
    path('show_posts/', ShowPosts.as_view(), name='posts_show'),
    path('create/', PostCreate.as_view(), name='post_create'),
]
