from django.urls import path

from statistic.views import RetrieveProfileAPIView, CreateFollowersAPIView

urlpatterns = [
    path('profile/', RetrieveProfileAPIView.as_view(), name='profile'),
    path('follow/', CreateFollowersAPIView.as_view(), name='follow')
]