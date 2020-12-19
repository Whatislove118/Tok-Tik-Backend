from django.urls import path

from profilesettings.views import *

urlpatterns = [
    path('', profile_settings),
    path('avatar/', avatar),
    path('confidentiality/', confidentiality),
    path('security/', security),
    path('default/', default_profile_settings)
]