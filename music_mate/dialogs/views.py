from django.db.models import Q

from drf_spectacular.utils import extend_schema

from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.views import exception_handler
from rest_framework.viewsets import ModelViewSet

from dialogs.models import Dialog
from dialogs.serializers import DialogSerializer, MessageSerializer
from dialogs.services import MatchChecker
from users.models import CustomUser


@extend_schema(tags=['Dialogs'])
class DialogViewSet(ModelViewSet):
    """Вьюсет для управления диалогами"""
    serializer_class = DialogSerializer
    queryset = Dialog.objects.all()

    def create(self, request, *args, **kwargs):
        """Метод скопирован с оригинальном и отредактирован -
        добавлена проверка на наличие Match перед созданием
        диалога."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        companion_user = CustomUser.objects.get(pk=self.kwargs['pk'])
        checker = MatchChecker()
        if checker.check_if_dialog_exists(self.request.user, companion_user):
            return Response({}, status=status.HTTP_200_OK)

        elif checker.check_match(self.request.user, companion_user):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        return Response({'errors': 'Без взаимного отклика личная перписка недоступна.'},
                        status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_context(self):
        """Передаем текущего пользователя и
        его собеседника в контекст сериализатора
        для будущей работы с методом create."""
        context = super().get_serializer_context()
        context['current_user'] = self.request.user
        context['companion_id'] = self.kwargs['pk']
        return context

    def perform_create(self, serializer):
        """Если диалога между двумя конкретными пользователями
        еще нет - его нужно создать, иначе - вернуть уже существующий."""
        current_user = self.request.user
        companion_user = CustomUser.objects.get(id=self.kwargs['pk'])
        # messages_count = Dialog
        serializer.save(started_by=current_user, to_whom=companion_user)

    def handle_exception(self, exc):
        """Обработка вызванной в сериализаторе ошибки - при
        попытке создать диалог в отсутствие match."""
        if isinstance(exc, ValidationError):
            return Response(exc.detail, status=status.HTTP_400_BAD_REQUEST)
        return exception_handler(exc, self)


@extend_schema(tags=['Dialogs'])
class MessageViewSet(ModelViewSet):
    """Класс для управления личными переписками."""
    serializer_class = MessageSerializer

    def get_dialog(self):
        return Dialog.objects.filter(Q(started_by=self.request.user) |
                                     Q(to_whom=self.request.user)).get(
            id=self.kwargs['pk'])

    def get_queryset(self):
        """Allows both participants
        to access the same dialog."""
        dialog = self.get_dialog()
        return dialog.related_messages.all()

    def perform_create(self, serializer):
        dialog = self.get_dialog()
        serializer.save(author=self.request.user, dialog=dialog)
