from django.urls import path, include

from accounts.views import CreateUpdateUserAPIView

urlpatterns = [
    path('', CreateUpdateUserAPIView.as_view(), name='register'),
    path('auth/', include('djoser.urls.jwt')),

]