from rest_framework.serializers import ModelSerializer, SerializerMethodField
from course.models import Course, Lesson, Payments


class CourseSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    count_lessons = SerializerMethodField()
    lessons = LessonSerializer(source="lesson_set", many=True)

    def get_count_lessons(self, instance):
        return instance.lesson_set.count()

    class Meta:
        model = Course
        fields = ("name", "img", "description", "lessons", "count_lessons")


class PaymentsSerializer(ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"
