# Generated by Django 3.2.18 on 2023-04-10 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_rename_topicmessage_forumtopicmessage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forumsectiontopic',
            name='number_of_messages',
        ),
        migrations.AddField(
            model_name='forumtopicmessage',
            name='number_of_messages',
            field=models.IntegerField(default=1, verbose_name='Количество сообщений в теме'),
            preserve_default=False,
        ),
    ]
