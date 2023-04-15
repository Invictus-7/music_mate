from django.db.models import Q
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework.serializers import ValidationError

from dialogs.models import Dialog, Message
from feed.models import Match
from users.models import CustomUser


class DialogSerializer(ModelSerializer):
    # number_of_messages = SerializerMethodField()

    class Meta:
        model = Dialog
        fields = ('id', 'started_by', 'to_whom', 'date_started', 'number_of_messages')

        read_only_fields = ('started_by', 'to_whom', 'date_started', 'number_of_messages')

    def create(self, validated_data):  # УДАЛИТЬ ЕГО
        """Перед созданием диалога сначала проводим проверку
         на взаимный match, а затем убеждаемся, что диалога
        с такими же собеседниками еще не существует."""
        current_user = self.context['current_user']
        companion_user = CustomUser.objects.get(pk=self.context['companion_id'])

        if Match.objects.filter(Q(matcher=current_user, matched=companion_user) and
                                Q(matched=companion_user, matcher=current_user)).exists():

            dialog = Dialog.objects.filter(Q(started_by=current_user, to_whom=companion_user) |
                                           Q(started_by=companion_user, to_whom=current_user))

            if dialog.exists():
                return dialog.first()
            else:
                return Dialog.objects.create(started_by=current_user, to_whom=companion_user)

        else:
            raise ValidationError(detail='Без взаимного отклика личная перписка недоступна.')

    # def get_number_of_messages(self):
    #     """Получаем количество сообщений в конкретном диалоге."""
    #     current_user = self.context['current_user']
    #     companion_user = CustomUser.objects.get(pk=self.context['companion_id'])
    #     target_dialog = Dialog.objects.filter(Q(started_by=current_user, to_whom=companion_user) |
    #                                           Q(started_by=companion_user, to_whom=current_user))
    #
    #     return target_dialog.related_messages.all().count()


class MessageSerializer(ModelSerializer):

    class Meta:
        model = Message
        fields = ('id', 'author', 'text', 'date_sent', 'dialog')
        read_only_fields = ('author', 'date_sent', 'dialog')
