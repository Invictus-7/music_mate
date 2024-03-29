from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import UserManager

from django.db import models


class CustomUser(AbstractBaseUser):
    """Модель базового пользователя сайта."""
    username = models.CharField('Имя пользователя', max_length=100, unique=True)
    email = models.EmailField('E-mail', max_length=150, unique=True)
    date_registered = models.DateTimeField('Дата регистрации', auto_now_add=True)
    is_staff = models.BooleanField('Модератор', default=False)  # staff - модератор форума
    is_superuser = models.BooleanField('Администратор', default=False)
    is_ensemble = models.BooleanField('Ансамбль', default=False)
    # насчет рейтинга - см. п. 1 файла Notices.txt
    # personal_rating = models.ManyToManyField(...)

    USERNAME_FIELD = 'username'

    # поля, без которых POST-запрос
    # на регистрацию пользователя не обработается
    REQUIRED_FIELDS = ['email', 'password', 'is_ensemble']

    objects = UserManager()

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'],
                name='уникальные пользователи'
            )
        ]

    def __str__(self):
        if self.is_ensemble:
            return f'{self.username} - музыкальный коллектив'
        else:
            return f'{self.username} - музыкант'







