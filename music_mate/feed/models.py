from django.db import models

from users.models import CustomUser


class FeedAdv(models.Model):
    """Модель объявления для ленты."""
    name = models.CharField('Имя/Название', max_length=200)
    city = models.CharField('Город', max_length=100)
    style = models.CharField('Стили музыки', max_length=100)
    instruments = models.ManyToManyField('Instrument', through='AdvInstrument',
                                         related_name='adverts')

    date_created = models.DateTimeField(auto_now_add=True)
    number_of_members = models.IntegerField()
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class Instrument(models.Model):
    """Модель инструмента."""
    name = models.CharField('Инструмент', max_length=255)
    degree = models.CharField('Уровень владения', max_length=255)

    def __str__(self):
        return self.name


class AdvInstrument(models.Model):
    """Промежуточная модель - музыкант-инструмент для связи M2M."""
    adv = models.ForeignKey(FeedAdv, on_delete=models.CASCADE, verbose_name='объявление',
                            related_name='feed_adv')
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE, verbose_name='инструмент',
                                   related_name='instrument')


class Match(models.Model):
    """Определяет пересечение (взаимность) откликов для того,
    чтобы разрешать/запрещать доступ к личной переписке."""

    matcher = models.ForeignKey(CustomUser, related_name='outgoing_matches',
                                on_delete=models.CASCADE, verbose_name='Кто откликнулся')
    matched = models.ForeignKey(CustomUser, related_name='incoming_matches',
                                on_delete=models.CASCADE, verbose_name='На кого откликнулись')

    class Meta:
        unique_together = ('matcher', 'matched')
