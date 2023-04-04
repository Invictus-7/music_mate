
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import (ModelSerializer,
                                        SerializerMethodField,
                                        StringRelatedField
                                        )

from music_mate import settings

from feed.models import FeedAdv
from forum.models import ForumSection, TopicMessage, ForumSectionTopic


class FeedAdvSerializer(ModelSerializer):
    """Сериализатор для ленты музыкантов."""
    class Meta:
        model = FeedAdv
        fields = (
            'name', 'city', 'style', 'instruments',
            'date_created', 'number_of_members'
        )
        read_only_fields = ('user',)

    def validate(self, data):
        """Проверяется соответствие типа пользователя
        и количества участников."""
        # получаем объект пользователя из контекста сериализатора
        user = self.context['request'].user

        if data['number_of_members'] == 0:
            raise ValidationError(settings.ZERO_MEMBERS_MSG)

        if user.is_ensemble:
            if data['number_of_members'] < 2:
                raise ValidationError(settings.NOT_ENOUGH_MEMBERS_MSG)
        else:
            if data['number_of_members'] > 1:
                raise ValidationError(settings.TOO_MUCH_MEMBERS_MSG)

        return data


class TopicTitleIdSerializer(ModelSerializer):
    class Meta:
        model = ForumSectionTopic
        fields = ('id', 'title')


class ForumSectionSerializer(ModelSerializer):
    """Сериализатор для просмотра содержимого разделов форума."""
    # topics = StringRelatedField(read_only=True, many=True)
    topics = SerializerMethodField()

    class Meta:
        model = ForumSection
        fields = ('title', 'date_created', 'created_by',
                  'number_of_topics', 'topics')

    def get_topics(self, obj):
        """Создает список словарей в поле topics."""
        section_related_topics = obj.topics.all()
        serialize_id_title = TopicTitleIdSerializer(section_related_topics, many=True)
        return serialize_id_title.data


class ForumSectionTopicSerializer(ModelSerializer):
    """Сериализатор для просмотра содержимого тем форума."""
    forum_section = StringRelatedField(read_only=True)

    class Meta:
        model = ForumSectionTopic
        fields = ('title', 'date_created', 'created_by',
                  'number_of_messages', 'forum_section', 'messages')


class TopicMessageSerializer(ModelSerializer):
    """Сериализатор для сообщений форума."""
    class Meta:
        model = TopicMessage
        fields = ('text', 'date_created',
                  'forum_topic')
