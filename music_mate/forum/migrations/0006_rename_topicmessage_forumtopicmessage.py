# Generated by Django 3.2.18 on 2023-04-09 18:36

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0005_auto_20230406_1753'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TopicMessage',
            new_name='ForumTopicMessage',
        ),
    ]
