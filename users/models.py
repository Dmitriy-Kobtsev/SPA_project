from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите почту"
    )
    phone = models.CharField(
        max_length=150, verbose_name="Телефон", null=True, blank=True
    )
    city = models.CharField(max_length=150, verbose_name="Город")
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="Авартарка",
        null=True,
        blank=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [""]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Donation(models.Model):
    amount = models.PositiveIntegerField(
        verbose_name="Сумма платежа",
        help_text="Укажите сумму платежа"
    )
    session_id = models.CharField(
        max_length=255,
        verbose_name="Id сессии",
        help_text="Укажите id сессии",
        null=True,
        blank=True,
    )
    link = models.URLField(
        max_length=400,
        verbose_name="Ссылка на оплату",
        help_text="Укажите ссылку на оплату",
        null=True,
        blank=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="Пользователь",
        help_text="укажите пользователя",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "платеж"
        verbose_name_plural = "платежи"

    def __str__(self):
        return self.amount
