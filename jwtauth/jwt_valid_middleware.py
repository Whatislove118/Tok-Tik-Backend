from django.http import HttpResponse
from jwt import DecodeError, ExpiredSignatureError
from rest_framework import status

from jwtauth.utils import *

class ValidJWTMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        if request.path != '/users/' and request.path != '/users/auth/':
            print('access_token required')
            access_token = request.headers.get('Access-Token')
            print(access_token)
            print('middleware check access_token: {}'.format(access_token))
            try:
                if validate_access_token(access_token):
                    print('middleware checked access_token: True')
                    response = self.get_response(request)
                else:
                    print('middleware cant checked access_token: False')
                    return HttpResponse('You dont have access_token', status=status.HTTP_401_UNAUTHORIZED, )
            except DecodeError:
                return HttpResponse('You dont have access_token', status=status.HTTP_401_UNAUTHORIZED, )
            except ExpiredSignatureError:
                return HttpResponse('Signature has expired', status=status.HTTP_408_REQUEST_TIMEOUT)
        else:
            print('access_token not required')
            response = self.get_response(request)
        return response





