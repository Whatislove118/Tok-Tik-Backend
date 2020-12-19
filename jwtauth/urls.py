from django.urls import path

from jwtauth.views import refresh_token

urlpatterns = [
    # path('create/'),
    path('refresh/', refresh_token),
]