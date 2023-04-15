from django.urls import path

from feed.views import MatchViewSet

urlpatterns = [
    path('respond_adv/<int:pk>', MatchViewSet.as_view({'post': 'create'}), name='respond_adv')
]
