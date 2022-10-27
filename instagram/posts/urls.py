from django.urls import path

from accounts.views import LoginView, logout_view, RegisterView, ProfileView, UserChangeView
from posts.views import PostView

urlpatterns = [
    path('/', PostView.as_view(), name='index'),
]
