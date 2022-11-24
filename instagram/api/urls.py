from rest_framework import routers
from django.urls import path, include

from api.views import PostViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
app_name = 'api'

urlpatterns = [
    path('', include(router.urls), name='api_posts'),
]
