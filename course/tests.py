from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from course.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test_user@mail.ru")
        self.course = Course.objects.create(name="Django", description="Изучаем фреймворк")
        self.lesson = Lesson.objects.create(name="ORM", course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        """Тестирование просмотра урока"""
        url = reverse("course:lessons_retrieve", args=(self.lesson.pk,))

        response = self.client.get(url)
        data = response.json()

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("name"),
            self.lesson.name
        )

    def test_lesson_create(self):
        url = reverse("course:lessons_create")
        data = {
            "name": "Forms",
            "description": "Example www.youtube.com/123"
        }

        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Lesson.objects.all().count(),
            2
        )

    def test_lesson_update(self):
        url = reverse("course:lessons_update", args=(self.lesson.pk,))

        date = {
            "name": "Forms_2.0"
        }

        response = self.client.patch(url, date)
        data = response.json()

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            data.get("name"),
            "Forms_2.0"
        )

    def test_lesson_destroy(self):
        url = reverse("course:lessons_delete", args=(self.lesson.pk,))

        response = self.client.delete(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            Lesson.objects.all().count(),
            0
        )

    def test_lesson_list(self):
        url = reverse("course:lessons")
        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_subscription_create(self):
        url = reverse("course:subscription")
        data = {
            "user": self.user.pk,
            "course": self.course.pk
        }
        response = self.client.post(url, data)
        data_response = response.json()

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            data_response.get('message'),
            'подписка добавлена'
        )

        response = self.client.post(url, data)
        data = response.json()

        self.assertEqual(
            data.get('message'),
            'подписка удалена'
        )
