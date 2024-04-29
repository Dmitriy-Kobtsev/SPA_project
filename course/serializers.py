from rest_framework.serializers import ModelSerializer, SerializerMethodField

from course.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(ModelSerializer):
    count_course_lessons = SerializerMethodField()

    def get_count_course_lessons(self, course):
        return Course.object.filter(lesson=course.lesson).count

    class Meta:
        model = Course
        fields = ("name", "img", "description")


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'