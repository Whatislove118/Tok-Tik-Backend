import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.request import Request
from rest_framework.response import Response
from .serializer import *
from jwtauth.utils import get_user_id_from_payload


def get_user_id_from_request(request):
    access_token = request.headers.get('Access-Token')
    return get_user_id_from_payload(access_token)

@api_view(['POST'])
def default_profile_settings(request: Request):
    user_id = get_user_id_from_request(request)
    profile_settings_obj = ProfileSettings.objects.get(id=user_id)
    avatar_obj = Avatar(name='default_img', url='/static/default_img.png/', id=profile_settings_obj)
    avatar_obj.save()

    data = {
        'url': avatar_obj.url
    }
    print(avatar_obj.url)
    return Response(data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def profile_settings(request: Request):
    user_id = get_user_id_from_request(request)
    profile_settings = request.data.get('profile-settings')
    serializer_profile_settings = ProfileSettingsSerializer(data=profile_settings)

    if serializer_profile_settings.is_valid():
        data = {
            'push_notifications': serializer_profile_settings.data.get('push_notifications')
        }
        profile_settings = ProfileSettings.objects.get(id=user_id)
        if serializer_profile_settings.data.get('username') is not None:
            print(1)
            data['username'] = serializer_profile_settings.data.get('username')
            print(data)
        saved_profile_settings = serializer_profile_settings.update(profile_settings, data)
    return Response(status=status.HTTP_200_OK)


@api_view(['PUT'])
@parser_classes([MultiPartParser,])
def avatar(request):
    user_id = get_user_id_from_request(request)
    profile_settings = ProfileSettings.objects.get(id=user_id)
    avatar_img = request.data.get('avatar')
    data = {
        'url': '/static/{}/'.format(avatar_img),
    }
    avatar = Avatar(name=avatar_img, url=data.get('url'), id=profile_settings)
    avatar.save()
    return Response(data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def confidentiality(request):
    user_id = get_user_id_from_request(request)
    confidentiality = request.data.get('confidentiality')
    serializer_confidentiality = ConfidentialitySerializer(data=confidentiality)
    if serializer_confidentiality.is_valid():
        data = {
            'private_account': serializer_confidentiality.data.get('private_account'),
            'allow_download_video': serializer_confidentiality.data.get('allow_download_video'),
            'comments_filter': serializer_confidentiality.data.get('comments_filter'),
            'allow_private_message': serializer_confidentiality.data.get('allow_private_message'),
            'allow_likes_list_looking': serializer_confidentiality.data.get('allow_likes_list_looking'),
        }
        confidentiality = Confidentiality.objects.get(id=user_id)
    return Response(status=status.HTTP_200_OK)

@api_view(['PUT'])
def security(request):
    user_id = get_user_id_from_request(request)
    security = request.data.get('security')
    serializer_security = SecuritySerializer(data=security)
    if serializer_security.is_valid():
        data = {
            'two_step_verification': serializer_security.data.get('two_step_verification'),
            'your_devices': serializer_security.data.get('your_devices'),
        }
        security = Security.objects.get(id=user_id)
        saved_security = serializer_security.update(security, data)
    return Response(status=status.HTTP_200_OK)