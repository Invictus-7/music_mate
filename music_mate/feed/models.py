from django.db import models

from users.models import CustomUser

CITY_CHOICES = (('Москва', 'Москва'), ('Владивосток', 'Владивосток'), ('Тюмень', 'Тюмень'))
STYLE_CHOICES = (('Rock', 'Rock'), ('Metal', 'Metal'), ('Jazz', 'Jazz'))
INSTRUMENTS = (('Vocal', 'Vocal'), ('Guitar', 'Guitar'), ('Piano', 'Piano'))


class FeedAdv(models.Model):
    """Модель объявления для ленты."""
    name = models.CharField('Имя/Название', max_length=200)
    # title - название группы, уникальное, заполняется обязательно, если is_ensemble=True
    city = models.CharField('Город',
                            max_length=max(len(city) for city, _ in CITY_CHOICES),
                            choices=CITY_CHOICES)
    style = models.CharField('Стиль музыки',
                             max_length=max(len(style) for style, _ in STYLE_CHOICES),
                             choices=STYLE_CHOICES)
    instruments = models.CharField('Инструменты',
                                   max_length=max(len(instrument) for instrument, _ in INSTRUMENTS),
                                   choices=INSTRUMENTS)

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





