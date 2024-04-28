from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name="Почта", help_text='Укажите почту')
    phone = models.CharField(max_length=150, verbose_name='Телефон', null=True, blank=True)
    city = models.CharField(max_length=150, verbose_name='Город')
    avatar = models.ImageField(upload_to='users/avatars', verbose_name='Авартарка', null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [""]

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
