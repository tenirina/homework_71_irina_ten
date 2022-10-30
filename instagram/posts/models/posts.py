from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    description = models.TextField(verbose_name='Description', null=False, blank=False, max_length=200)
    image = models.ImageField(verbose_name='Photo', null=True, blank=False, upload_to='posts')
    author = models.ForeignKey(verbose_name='Author', to=get_user_model(), related_name='posts', null=False, blank=False,
                               on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='Date of creation', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Date of change', auto_now=True)
