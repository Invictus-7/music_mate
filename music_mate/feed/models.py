from django.db import models

from users.models import CustomUser

from music_mate import constants


class FeedAdv(models.Model):
    """Модель объявления для ленты."""
    name = models.CharField('Имя/Название', max_length=200)
    city = models.CharField('Город')
    style = models.CharField('Стили музыки')
    instruments = models.CharField('Инструменты')

    date_created = models.DateTimeField(auto_now_add=True)
    number_of_members = models.IntegerField()
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class Match(models.Model):
    """Определяет пересечение (взаимность) откликов для того,
    чтобы разрешать/запрещать доступ к личной переписке."""

    matcher = models.ForeignKey(CustomUser, related_name='outgoing_matches',
                                on_delete=models.CASCADE, verbose_name='Кто откликнулся')
    matched = models.ForeignKey(CustomUser, related_name='incoming_matches',
                                on_delete=models.CASCADE, verbose_name='На кого откликнулись')

    class Meta:
        unique_together = ('matcher', 'matched')





