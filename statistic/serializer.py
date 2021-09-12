from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from statistic.models import UserStatistics, Followers


class UserStatisticsSerializer(ModelSerializer):
    class Meta:
        model = UserStatistics
        fields = ('amount_videos', 'likes_on_videos', 'count_followers')

class FollowersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Followers
        fields = '__all__'
        """ Так как мы получаем user_id из токена, то данное поле нам необходимо передавать в сериализаторе только при retrieve """
        read_only_fields = ['user_id']