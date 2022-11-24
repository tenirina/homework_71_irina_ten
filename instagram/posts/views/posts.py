from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, DetailView

from accounts.models import Account
from posts.forms import PostForm
from posts.models import Post


class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = 'posts/create.html'
    form_class = PostForm
    model = Post

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')


class PostView(DetailView):
    template_name = "posts/post.html"
    model = Post
    fields = ('image', 'description',)


class SubscribeView(View):

    def post(self, request, *args, **kwargs):
        sub_user = request.user
        user = Account.objects.get(pk=kwargs.get('pk'))
        if not sub_user.subscriptions.filter(username=user).exists():
            sub_user.subscriptions.add(user)
            sub_user.count_subscriptions += 1
            sub_user.save()
            user.count_subscribers += 1
            user.save()
        elif sub_user.subscriptions.filter(username=user):
            sub_user.subscriptions.remove(user)
            sub_user.count_subscriptions -= 1
            sub_user.save()
            user.count_subscribers -= 1
            user.save()
        return redirect('profile', pk=kwargs.get('pk'))


class LikeView(View):

    def get(self, request, *args, **kwargs):
        user = request.user
        post = get_object_or_404(Post, pk=kwargs.get('pk'))
        if not post.user_likes.filter(username=user).exists():
            user.liked_posts.add(post)
            post.count_like += 1
            post.save()
        elif post.user_likes.filter(username=user):
            user.liked_posts.remove(post)
            post.count_like -= 1
            post.save()
        return redirect('index')
