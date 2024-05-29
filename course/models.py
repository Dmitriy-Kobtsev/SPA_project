from django.contrib.auth import get_user_model
from django.db import models

from users.models import User


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name="Курс")
    img = models.ImageField(
        upload_to="course/",
        verbose_name="Превью(картинка)",
        null=True,
        blank=True
    )
    description = models.TextField(
        verbose_name="Описание",
        null=True, blank=True
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="автор курса",
    )
    followers = models.ManyToManyField(
        User,
        verbose_name="Подписчики",
        related_name="user_followers",
        null=True,
        blank=True
    )

    def __str__(self):
        # Строковое отображение объекта
        return f"{self.name}: {self.description}"

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"


class Lesson(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="название урока"
    )
    description = models.TextField(
        verbose_name="описание урока",
        null=True, blank=True
    )
    img = models.ImageField(
        upload_to="course/lessons",
        verbose_name="превью (картинка)",
        null=True,
        blank=True,
    )
    video = models.FileField(
        upload_to="lessons/video",
        verbose_name="видео",
        null=True,
        blank=True
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="курс",
        null=True,
        blank=True
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name="автор"
    )

    def __str__(self):
        return f"Урок {self.name}"

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"


class Payments(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        verbose_name="Пользователь",
        null=True,
        blank=True,
    )
    date_pay = models.DateField(
        verbose_name="дата оплаты",
        auto_now_add=True
    )
    paid_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name="оплаченный урок",
        null=True,
        blank=True,
    )
    paid_course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="оплаченный курс",
        null=True,
        blank=True,
    )
    payment_amount = models.PositiveIntegerField(verbose_name="сумма оплаты")
    CHOICES = (
        ("1", "Cash"),
        ("2", "Transfer"),
    )
    payment_method = models.CharField(
        max_length=300,
        choices=CHOICES
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

    def __str__(self):
        return f"Урок {self.user} дата оплаты {self.date_pay}"

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"


class Subscription(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        verbose_name="Пользователь",
        null=True,
        blank=True,)
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name='курс',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "подписка"
        verbose_name_plural = "подписки"
