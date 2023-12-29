from django.urls import path
from . import views






app_name = 'posts'

urlpatterns = [
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('post/<slug:post_slug>', views.get_post, name='post'),
]
