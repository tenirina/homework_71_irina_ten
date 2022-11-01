from django.urls import path

from posts.views.base import IndexView
from posts.views.posts import CreateView, SubscribeView, LikeView
from posts.views.search import SearchView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('posts/search/', SearchView.as_view(), name='posts_search'),
    path('posts/create/', CreateView.as_view(), name='create_post'),
    path('posts/subscribe/<int:pk>', SubscribeView.as_view(), name='subscribe'),
    path('posts/like/<int:pk>', LikeView.as_view(), name='like')
]
