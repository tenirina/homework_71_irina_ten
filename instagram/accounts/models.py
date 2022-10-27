from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import TextChoices

from accounts.managers import UserManager


class GenderChoices(TextChoices):
    MALE = 'MALE', 'Man'
    FEMALE = 'FEMALE', 'Women'


class Account(AbstractUser):
    email = models.EmailField(
        verbose_name='Email',
        unique=True,
        blank=True,
        max_length=25
    )
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='avatars',
        verbose_name='Avatar',
        max_length=100
    )
    birthday = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата рождения'
    )
    liked_posts = models.ManyToManyField(
        verbose_name='Понравившиеся публикации',
        to='posts.Post',
        related_name='user_likes'
    )
    subscriptions = models.ManyToManyField(
        verbose_name='Подписки',
        to='accounts.Account',
        related_name='subscribers'
    )
    commented_posts = models.ManyToManyField(
        verbose_name='Прокомментированные публикации',
        to='posts.Post',
        related_name='user_comments'
    )
    description = models.TextField(
        verbose_name='Description',
        null=True,
        blank=True,
        max_length=150
    )
    phone = models.CharField(
        verbose_name='Phone',
        null=True,
        blank=True,
        max_length=15
    )
    gender = models.CharField(
        verbose_name='Gender',
        choices=GenderChoices.choices,
        default=GenderChoices.MALE,
        max_length=10
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'{self.username} profile'
