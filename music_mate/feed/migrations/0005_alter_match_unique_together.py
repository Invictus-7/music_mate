# Generated by Django 3.2.18 on 2023-04-14 06:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed', '0004_match'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='match',
            unique_together={('matcher', 'matched')},
        ),
    ]
