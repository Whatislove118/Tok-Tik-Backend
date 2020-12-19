from rest_framework.serializers import ModelSerializer

from statistic.models import UserStatistics


class UserStatisticsSerializer(ModelSerializer):
    class Meta:
        model = UserStatistics
        fields = ('amount_videos', 'likes_on_videos', 'count_followers')
