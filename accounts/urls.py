from django.urls import path

from accounts.views import register, authenticate_user, profile, follow

urlpatterns = [
    path('', register),
    path('auth/', authenticate_user),
    path('profile/', profile),
    path('follow/', follow)

]