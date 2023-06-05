from django.db import models

from users.models import CustomUser


class Dialog(models.Model):
    """Модель диалога - переписки между
    двумя пользователями."""
    started_by = models.ForeignKey(CustomUser, related_name='outgoing_dialogs',
                                   null=True, on_delete=models.SET_NULL)
    to_whom = models.ForeignKey(CustomUser, related_name='incoming_dialogs',
                                null=True, on_delete=models.SET_NULL)
    date_started = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['date_started']
        verbose_name = 'Диалог'
        verbose_name_plural = 'Диалоги'

    def __str__(self):
        return f'Переписка {self.started_by} и {self.to_whom}'


class Message(models.Model):
    """Модель личного сообщения."""
    author = models.ForeignKey(CustomUser, related_name='dialog_messages',
                               null=True, on_delete=models.SET_NULL)
    text = models.TextField('Текст сообщения')
    date_sent = models.DateTimeField('Дата и время отправки', auto_now_add=True)
    dialog = models.ForeignKey(Dialog, related_name='related_messages',
                               on_delete=models.CASCADE)

    class Meta:
        ordering = ['date_sent']
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.text[:30]



