from rest_framework.serializers import (
                                        ModelSerializer,
                                        SerializerMethodField,
                                        StringRelatedField
                                        )

from forum.models import ForumSection, ForumSectionTopic, ForumTopicMessage


class ForumSectionSerializer(ModelSerializer):
    """Сериализатор для просмотра стартовой страницы форума."""
    topics = SerializerMethodField()

    class Meta:
        model = ForumSection
        fields = ('id', 'title', 'date_created',
                  'topics', 'slug')
        read_only_fields = ('created_by',)

    def get_topics(self, obj) -> dict:
        """Создает список словарей в поле topics."""
        section_related_topics = obj.topics.all()
        serialize_id_title = TopicTitleIdSerializer(section_related_topics, many=True)
        return serialize_id_title.data


class TopicTitleIdSerializer(ModelSerializer):
    """Сериалайзер для отдачи на фронтенд
    списка словарей с топиками."""
    class Meta:
        model = ForumSectionTopic
        fields = ('id', 'title')


class ForumSectionTopicsSerializer(ModelSerializer):
    class Meta:
        model = ForumSectionTopic
        fields = ('id', 'title', 'date_created', 'created_by',
                  'forum_section', 'slug')
        read_only_fields = ('created_by', 'forum_section')


class ForumTopicMessageSerializer(ModelSerializer):
    forum_topic = StringRelatedField()

    class Meta:
        model = ForumTopicMessage
        fields = ('id', 'text', 'date_created', 'user', 'forum_topic')
        read_only_fields = ('user', 'forum_topic')

    def update(self, instance, validated_data):
        """Настраиваем возможность редактировать текст сообщения
        на уровне сериализатора."""
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance


