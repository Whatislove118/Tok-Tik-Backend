from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from djoser import permissions as dj_permissions
from rest_framework.permissions import IsAuthenticated


from profilesettings.models import ProfileSettings
from profilesettings.serializer import ProfileSettingsSerializer
from statistic.models import Followers
from statistic.serializer import FollowersSerializer

""" Класс для получения профиля юзера по его id"""
class RetrieveProfileAPIView(generics.RetrieveAPIView):
    permission_classes = [dj_permissions.CurrentUserOrAdmin, ]
    serializer_class = ProfileSettingsSerializer
    model = ProfileSettings
    lookup_field = 'id'
    queryset = ProfileSettings.objects.all()


class CreateFollowersAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = FollowersSerializer
    model = Followers
