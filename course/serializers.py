from rest_framework.serializers import ModelSerializer, SerializerMethodField

from course.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(ModelSerializer):
    count_lessons = SerializerMethodField()

    def get_count_lessons(self, instance):
        return instance.lesson_set.count()

    class Meta:
        model = Course
        fields = ("name", "img", "description", "count_lessons")


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'