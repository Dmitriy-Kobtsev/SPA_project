from rest_framework.serializers import ModelSerializer

from course.serializers import PaymentsSerializer
from users.models import User


class UserSerializer(ModelSerializer):
    payments = PaymentsSerializer(source="payments_set", many=True)

    class Meta:
        model = User
        fields = "__all__"


class UserDetailSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ["email", "phone", "city", "avatar"]
