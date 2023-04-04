from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer


from music_mate import settings

from feed.models import FeedAdv


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



