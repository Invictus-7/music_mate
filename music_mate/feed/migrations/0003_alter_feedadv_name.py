# Generated by Django 4.1.7 on 2023-04-03 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_alter_feedadv_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedadv',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Имя/Название'),
        ),
    ]
