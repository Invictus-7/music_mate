from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

from feed.views import FeedAdvViewSet, FeedReactView, ReactMatchViewSet
from users.views import UserViewSet

router_v1 = DefaultRouter()

router_v1.register('users', UserViewSet, basename='users')
router_v1.register('feed', FeedAdvViewSet, basename='feed')

urlpatterns = [
    path('api/v1/auth/', include(router_v1.urls)),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
    # Конфигурация DRF_Spectacular для просмотра документации
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema')),

    path('api/v1/admin/', admin.site.urls),
    path('api/v1/feed/', include('feed.urls')),
    path('api/v1/forum/', include('forum.urls')),
    path('api/v1/dialogs/', include('dialogs.urls')),
    # React Test
    path('api/bands/show', FeedReactView.as_view({'get': 'list'})),
    path('api/feed/respond_adv/check', ReactMatchViewSet.as_view({'post': 'create'})),
    re_path(r"^.*$", TemplateView.as_view(template_name="index.html"))

]

# Настройки для хранения статики и файлов
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )



