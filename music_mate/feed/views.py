from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from feed.models import FeedAdv
from .serializers import FeedAdvSerializer


class FeedAdvViewSet(ModelViewSet):
    """Вьюсет для создания и просмотра объявлений."""
    serializer_class = FeedAdvSerializer
    permission_classes = (IsAuthenticated,)

    def get_serializer_context(self):
        """Добавляем объект request в словарь контекста, чтобы
        в дальнейшем передать его в метод validate()
        сериализатора для валидации по типу пользователя
        (музыкант или ансамбль)."""
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def perform_create(self, serializer):
        """Автоматическое установка текущего пользователя
        в качестве создателя объявления."""
        serializer.save(user=self.request.user)

    @action(
        methods=('GET',),
        detail=False,
        url_path='show',
        permission_classes=(IsAuthenticated,)
    )
    def display_feed(self, request):
        """Возвращает в ленту все группы, если на сайте залогинился
        музыкант, и всех музыкантов, если залогинилась группа."""
        user = request.user
        to_display = FeedAdv.objects.all().exclude(user__is_ensemble=user.is_ensemble)
        serializer = FeedAdvSerializer(to_display, many=True)
        if user.is_ensemble:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_200_OK)
