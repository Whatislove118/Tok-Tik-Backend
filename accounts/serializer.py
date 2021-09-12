from rest_framework import serializers


from accounts.models import User
from statistic.models import Followers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('login', 'password', 'email', 'id')
        read_only_fields = ['id']




