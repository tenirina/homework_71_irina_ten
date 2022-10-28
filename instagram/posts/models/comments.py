from django.contrib.auth import get_user_model
from django.db import models


class Comment(models.Model):
    author = models.ForeignKey(verbose_name='Author', to=get_user_model(), related_name='comments', null=False,
                               blank=False, on_delete=models.CASCADE)
    post = models.ForeignKey(verbose_name='Post', to='posts.Post', related_name='comments', null=False,
                             blank=False, on_delete=models.CASCADE)
    text = models.CharField(verbose_name='Text', null=False, blank=False, max_length=200)
