from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from forum.models import ForumSection, ForumSectionTopic, ForumTopicMessage
from forum.permissions import IsModerator, IsSuperUser
from forum.serializers import (
                             ForumSectionSerializer,
                             ForumSectionTopicsSerializer,
                             ForumTopicMessageSerializer
                             )


@extend_schema(tags=['Forum_Index'])
class ForumIndexViewSet(ModelViewSet):
    """Вьюсет для стартовой страницы форума -
    списка разделов."""
    serializer_class = ForumSectionSerializer
    queryset = ForumSection.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated(), IsModerator()]
        elif self.action == 'destroy':
            return [IsAuthenticated(), IsSuperUser()]
        else:
            return []

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


@extend_schema(tags=['Forum_Section_Topics'])
class ForumSectionTopicsViewSet(ModelViewSet):
    """Вьюсет для работы с темами внутри раздела."""
    serializer_class = ForumSectionTopicsSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        """Разный набор объектов в зависимости от вида запроса."""
        if self.request.method == 'GET':
            print(ForumSectionTopic.objects.filter(forum_section__slug=self.kwargs['slug']))
            return ForumSectionTopic.objects.filter(forum_section__slug=self.kwargs['slug'])
        if self.request.method == 'DELETE':
            return ForumSectionTopic.objects.filter(slug=self.kwargs['slug'])

    def get_permissions(self):
        """Создавать темы может любой аутентифицированный
        пользователь, удалять - только модератор."""
        if self.action == 'create':
            return [IsAuthenticated()]
        elif self.action == 'destroy':
            return [IsAuthenticated(), IsModerator()]
        else:
            return []

    def perform_create(self, serializer):
        """Автоматически присваиваем теме
        раздел и автора при её создании."""
        current_section = ForumSection.objects.get(slug=self.kwargs['slug'])
        serializer.save(created_by=self.request.user,
                        forum_section_id=current_section.id)


@extend_schema(tags=['Forum_Topic_Messages'])
class ForumTopicMessageView(ModelViewSet):
    serializer_class = ForumTopicMessageSerializer

    def get_queryset(self):
        return ForumTopicMessage.objects.filter(forum_topic__slug=self.kwargs['slug'])

    def perform_create(self, serializer):
        related_topic = ForumSectionTopic.objects.get(slug=self.kwargs['slug'])
        serializer.save(user=self.request.user,
                        forum_topic_id=related_topic.id)

    def get_permissions(self):
        if self.action == 'destroy' or self.action == 'update':
            return [IsAuthenticated(), IsModerator()]
        return []












