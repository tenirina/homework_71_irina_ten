from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include

from api.views import PostViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
app_name = 'api'

urlpatterns = [
    path('', include(router.urls), name='api_posts'),
    path('posts/<int:pk>/like/', PostViewSet.as_view({'post': 'create_likes'}), name='like_create'),
    path('posts/<int:pk>/dislike/', PostViewSet.as_view({'delete': 'delete_likes'}), name='like_delete'),
    path('login/', obtain_auth_token, name='api_token_auth')
]
