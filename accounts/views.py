from django.contrib.auth import user_logged_in

# Create your views here.
from django.http import HttpRequest
from rest_framework import status, generics, viewsets, mixins
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from jwtauth.models import RefreshToken
from jwtauth.utils import *

from accounts.models import User
from accounts.serializer import UserSerializer, FollowersSerializer
from profilesettings.models import ProfileSettings
from profilesettings.serializer import ProfileSettingsSerializer
from statistic.models import Followers
from djoser import permissions as dj_permissions


""" Создаем с помощью миксинов класс APIView с необходимыми нами методами """
class CreateUpdateAPIView(mixins.CreateModelMixin, mixins.UpdateModelMixin, GenericAPIView):

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class CreateUpdateUserAPIView(CreateUpdateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = UserSerializer
    model = User

    """ Класс для определения permissions в зависимости от метода запроса"""
    def get_permissions(self):
        if self.request.method == 'PUT':
            self.permission_classes = [IsAuthenticated, ]
        return super().get_permissions()







