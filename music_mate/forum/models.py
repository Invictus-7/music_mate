from django.db import models

from users.models import CustomUser


class BaseForumModel(models.Model):
    """Общий класс для моделей
    'Раздел' и 'Тема' на форуме."""
    title = models.CharField('Название',
                             max_length=300)
    date_created = models.DateTimeField('Дата создания', auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    class Meta:
        abstract = True
        ordering = ('date_created',)


class ForumSection(BaseForumModel):
    """Модель 'Раздел' на форуме."""
    slug = models.SlugField('Короткое название раздела', max_length=50)

    def __str__(self):
        return f'Раздел {self.title}'


class ForumSectionTopic(BaseForumModel):
    """Модель 'Тема' на форуме."""
    forum_section = models.ForeignKey(ForumSection, related_name='topics',
                                      on_delete=models.CASCADE)
    slug = models.SlugField('Короткое название темы внутри раздела', max_length=50)

    def __str__(self):
        return f'Тема {self.title}'


class ForumTopicMessage(models.Model):
    text = models.TextField('Текст сообщения')
    date_created = models.DateTimeField('Дата написания', auto_now_add=True)
    user = models.ForeignKey(CustomUser, related_name='messages',
                             on_delete=models.DO_NOTHING)
    forum_topic = models.ForeignKey(ForumSectionTopic, related_name='messages',
                                    on_delete=models.CASCADE)

    def __str__(self):
        return self.text
