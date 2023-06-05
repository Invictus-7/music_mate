from django.db.models import Q
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from dialogs.models import Dialog, Message
from users.models import CustomUser


class DialogSerializer(ModelSerializer):

    class Meta:
        model = Dialog
        fields = ('id', 'started_by', 'to_whom', 'date_started')

        read_only_fields = ('started_by', 'to_whom', 'date_started')


class MessageSerializer(ModelSerializer):

    class Meta:
        model = Message
        fields = ('id', 'author', 'text', 'date_sent', 'dialog')
        read_only_fields = ('author', 'date_sent', 'dialog')
