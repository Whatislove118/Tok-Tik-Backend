from django.contrib.auth.backends import BaseBackend

class JwtBackend(BaseBackend):
    def authenticate(self, request, token=None, **kwargs):
        login = request.data.get('login')
        password = request.data.get('password')

