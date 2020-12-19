import datetime
import jwt
import base64

from django.conf import settings

from jwtauth.models import RefreshToken


def get_user_id_from_payload(token):
    payload = jwt.decode(token, settings.SECRET_KEY, algorithm='HS256')
    print(payload.get('user_id'))
    return payload.get('user_id')

def set_tokens_to_response(user):
    try:
        token = generate_access_token(user)
        refresh_token = generate_refresh_token(user)
        user_details = {}
        user_details['Access-Token'] = token
        refresh_token_object = RefreshToken.objects.create(user_id=user, last_login_in=datetime.datetime.today(),
                                                           refresh_token=refresh_token)
        RefreshToken.save(refresh_token_object)
        user_details['Refresh-Token'] = refresh_token
        return user_details
    except Exception as e:
        raise e

def get_user_id_from_token(token) -> int:
    payload = jwt.decode(token, settings.SECRET_KEY, algorithm='HS256')
    print(payload)
    user_id = payload.get('user_id')
    return user_id


def validate_access_token(token) -> bool:

    payload = jwt.decode(token, settings.SECRET_KEY, algorithm='HS256')
    server_token_signature = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
    if token == server_token_signature:
        return True
    else:
        return False



def check_exp_access_token(token) -> bool:

    access_token_payload = jwt.decode(token, settings.SECRET_KEY, algorithm='HS256')
    print(access_token_payload)
    exp = access_token_payload.get('exp')
    iat = int(datetime.datetime.utcnow().timestamp())
    print(iat)
    print(exp)
    if iat >= exp:
        return False
    else:
        return True

def generate_access_token(user) -> str:

    access_token_payload = {
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=60),
        'iat': datetime.datetime.utcnow(),
    }

    access_token = jwt.encode(access_token_payload,
                              settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
    return access_token


def generate_refresh_token(user):
    refresh_token_payload = {
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
        'iat': datetime.datetime.utcnow()
    }
    refresh_token = jwt.encode(
        refresh_token_payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')

    return refresh_token