from django.urls import path

from posts.views.base import IndexView
from posts.views.comments import CreateCommentView
from posts.views.posts import CreatePostView, SubscribeView, LikeView, PostView
from posts.views.search import SearchView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('posts/search/', SearchView.as_view(), name='posts_search'),
    path('posts/create/', CreatePostView.as_view(), name='create_post'),
    path('posts/subscribe/<int:pk>', SubscribeView.as_view(), name='subscribe'),
    path('posts/like/<int:pk>', LikeView.as_view(), name='like'),
    path('posts/comment/<int:pk>', CreateCommentView.as_view(), name='create_comment'),
    path('posts/post/<int:pk>', PostView.as_view(), name='post')
]
