from django.http import HttpResponse
from django.shortcuts import render

# Create your views here
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts.models import User
from jwtauth.models import RefreshToken
from jwtauth.utils import *


@api_view(['POST'])
def refresh_token(request):
    access_token = request.headers.get('Access-Token')
    refresh_token = request.headers.get('Refresh-Token')
    user_id = get_user_id_from_token(access_token)
    user = User.objects.get(id=user_id)
    refresh_token_server = RefreshToken.objects.get(user_id=user_id)
    if refresh_token == refresh_token_server:
        user_details = set_tokens_to_response(user)
        return Response(headers=user_details, status=status.HTTP_200_OK)

    return Response('Bad request', status=status.HTTP_403_FORBIDDEN)