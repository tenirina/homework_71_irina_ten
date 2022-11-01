from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from posts.models import Post


class IndexView(LoginRequiredMixin, ListView):
    login_url = 'accounts/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'index.html'
    ordering = ('-created_at',)
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        user = self.request.user
        authors = list(user.subscriptions.all())
        print(authors)
        posts = Post.objects.filter(author__in=authors)
        context['posts'] = posts
        return context




