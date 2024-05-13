from django.urls import path
from rest_framework.routers import SimpleRouter

from course.views import (
    CourseViewSet,
    LessonCreateAPIView,
    LessonListAPIView,
    LessonRetrieveAPIView,
    LessonDestroyAPIView,
    LessonUpdateAPIView,
    PaymentsListAPIView,
    SubscriptionAPIView,
)
from course.apps import CourseConfig

app_name = CourseConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("lessons/", LessonListAPIView.as_view(), name="lessons"),
    path(
        "lessons/<int:pk>/",
        LessonRetrieveAPIView.as_view(),
        name="lessons_retrieve"
    ),
    path(
        "lessons/create/",
        LessonCreateAPIView.as_view(),
        name="lessons_create"
    ),
    path(
        "lessons/<int:pk>/delete/",
        LessonDestroyAPIView.as_view(),
        name="lessons_delete",
    ),
    path(
        "lessons/<int:pk>/update/",
        LessonUpdateAPIView.as_view(),
        name="lessons_update"
    ),
    path("payments/", PaymentsListAPIView.as_view(), name="payments"),
    path("subscription/", SubscriptionAPIView.as_view(), name="subscription"),
]

urlpatterns += router.urls
