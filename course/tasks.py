import datetime

from celery import shared_task
from conf.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.utils import timezone

from users.models import User


@shared_task
def send_information_about_update_course(email, course):
    """
    Отправка сообщения пользователь об обновлении курса
    :param email: электронная почта
    :param course: курс который обновлен
    """
    send_mail(
        subject='Обновление курса',
        message=f'Наш курс {course} обновлен!',
        from_email=EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False,
    )


@shared_task
def block_user():
    """
    Блокирование пользователя если он не заходил больше месяца
    """

    today = timezone.now()
    users = User.objects.filter(is_active=True)
    print(type(today))
    print(today.date())
    if users.exists():
        for user in users:
            if user.last_login != None:
                if today - user.last_login > datetime.timedelta(weeks=4):
                    user.is_active = False
                    user.save()


