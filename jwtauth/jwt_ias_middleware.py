from django.http import HttpResponse
from rest_framework import status

from jwtauth.utils import *

class IasJWTMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        if request.path != '/users/' and request.path != '/users/auth/':
            print('check ias access_token')
            access_token = request.headers.get('Access-Token')
            print('middleware check ias access_token: {}'.format(access_token))
            if check_exp_access_token(access_token):
                print('middleware checked ias access_token: Token is active')
                response = self.get_response(request)
            else:
                print('middleware  checked ias access_token: Token is no active')
                return HttpResponse('Your access_token is no active', status=status.HTTP_401_UNAUTHORIZED)
        else:
            print('access_token ias not required')
            response = self.get_response(request)
        return response