from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from rest_framework_simplejwt import views as jwt_views

from .views import register

app_name = 'users'

urlpatterns = [
    path('user/', register, name='register_user'),
    path('test_cookie/', views.test_cookie, name='test_cookie'),

]