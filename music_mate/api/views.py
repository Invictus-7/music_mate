from djoser.views import UserViewSet as UserHandleSet

from rest_framework.viewsets import ModelViewSet


from forum.models import ForumSection, ForumSectionTopic

from .serializers import TopicMessageSerializer, ForumSectionSerializer, ForumSectionTopicSerializer


class UserViewSet(UserHandleSet):
    """Вьюсет для модели пользователя."""
    pass


class ForumIndexViewSet(ModelViewSet):
    """Отображает стартовую страницу форума -
    список разделов."""
    serializer_class = ForumSectionSerializer
    queryset = ForumSection.objects.all()


class ForumSectionTopicsViewSet(ModelViewSet):
    """Отображает содержимое раздела -
    список тем."""
    serializer_class = ForumSectionTopicSerializer
    lookup_url_kwarg = 'topic_id'
    lookup_field = 'id'

    def get_queryset(self):
        print(self.kwargs.get('id'))
        return ForumSection.objects.get(
            pk=self.kwargs.get('id')).topics


class TopicMessagesViewSet(ModelViewSet):
    """Отображает содержимое темы -
    список сообщений."""
    serializer_class = TopicMessageSerializer

    def perform_create(self, serializer):
        """Автоматическое установка текущего пользователя
        в качестве автора сообщения."""
        serializer.save(user=self.request.user)
