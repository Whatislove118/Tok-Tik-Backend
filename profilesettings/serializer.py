from rest_framework.serializers import ModelSerializer

from profilesettings.models import ProfileSettings, Avatar, Confidentiality, Security


class ProfileSettingsSerializer(ModelSerializer):
    class Meta:
        model = ProfileSettings
        fields = ('username', 'push_notifications')


class AvatarSerializer(ModelSerializer):
    class Meta:
        model = Avatar
        fields = ('name', 'url')

class ConfidentialitySerializer(ModelSerializer):
    class Meta:
        model = Confidentiality
        fields = ('private_account', 'allow_download_video',
                  'comments_filter', 'allow_private_message',
                  'allow_likes_list_looking')

class SecuritySerializer(ModelSerializer):
    class Meta:
        model = Security
        fields = ('two_step_verification', 'your_devices')

