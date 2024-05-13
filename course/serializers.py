from rest_framework import serializers
from course.models import Course, Lesson, Payments, Subscription
from course.validators import validate_url


class CourseSerializer(serializers.ModelSerializer):
    description = serializers.CharField(validators=[validate_url])

    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    description = serializers.CharField(validators=[validate_url])

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseDetailSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()
    subscription = serializers.SerializerMethodField()
    lessons = LessonSerializer(source="lesson_set", many=True, read_only=True)

    def get_subscription(self, instanse):
        request = self.context.get('request')
        user = None
        if request:
            user = request.user
        return instanse.subscription_set.filter(user=user).exists()

    def get_count_lessons(self, instance):
        return instance.lesson_set.count()

    class Meta:
        model = Course
        fields = ("name", "img", "description", "lessons", "count_lessons", "subscription")


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'