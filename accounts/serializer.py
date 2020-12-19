from rest_framework.serializers import Serializer, ModelSerializer

from accounts.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('login', 'password', 'email')


