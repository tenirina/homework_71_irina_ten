from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView

from posts.forms import CommentForm
from posts.models import Comment, Post


class CreateCommentView(LoginRequiredMixin, CreateView):
    template_name = 'comment/create.html'
    form_class = CommentForm
    model = Comment

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        form = self.get_form_class()(request.POST)
        comment = form.data.get('comment')
        user = request.user
        Comment.objects.create(author=user, text=comment, post=post)
        return redirect('index')

    def get_success_url(self):
        return redirect('index')


