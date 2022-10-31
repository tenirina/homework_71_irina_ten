from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    description = models.TextField(verbose_name='Description', null=False, blank=False, max_length=200)
    image = models.ImageField(verbose_name='Photo', null=True, blank=False, upload_to='posts')
    author = models.ForeignKey(verbose_name='Author', to=get_user_model(), related_name='posts', null=False, blank=False,
                               on_delete=models.CASCADE)
    count_like = models.IntegerField(verbose_name='Count like', default=0)
    count_comment = models.IntegerField(verbose_name='Count commentaries', default=0)
    created_at = models.DateTimeField(verbose_name='Date of creation', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Date of change', auto_now=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
