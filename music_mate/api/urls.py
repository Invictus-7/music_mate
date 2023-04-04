from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.decorators import action
from rest_framework.routers import DefaultRouter

from feed.views import FeedAdvViewSet
from api.views import (
                    UserViewSet,
                    ForumIndexViewSet,
                    ForumSectionTopicsViewSet,
                    TopicMessagesViewSet
                    )

router_v1 = DefaultRouter()

router_v1.register('users', UserViewSet, basename='users')
router_v1.register('feed', FeedAdvViewSet, basename='feed')
# выстроить последовательную цепь внутри маршрута forum/название секции/название темы
router_v1.register('forum_sections', ForumIndexViewSet, basename='forum_sections')
# router_v1.register('forum_sections/<int:section_id>',
#                    ForumSectionTopicsViewSet, basename='section_topics')
# router_v1.register('forum_sections/<int:topic_id>',
#                    ForumSectionTopicsViewSet, basename='section_topics')
router_v1.register('topic_messages', TopicMessagesViewSet, basename='topic_messages')


urlpatterns = [
    path('', include(router_v1.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # Конфигурация DRF_Spectacular для просмотра документации
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
]