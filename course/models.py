from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='Курс')
    img = models.ImageField(upload_to='course/', verbose_name='Превью(картинка)', null=True, blank=True)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name}: {self.description}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='название урока')
    description = models.TextField(verbose_name='описание урока', null=True, blank=True)
    img = models.ImageField(upload_to='course/lessons', verbose_name='превью (картинка)', null=True, blank=True)
    video = models.FileField(upload_to='lessons/video', verbose_name='видео', null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', null=True, blank=True)

    def __str__(self):
        return f'Урок {self.name}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'