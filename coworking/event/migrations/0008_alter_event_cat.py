# Generated by Django 4.1.1 on 2022-12-17 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_alter_event_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='cat',
            field=models.IntegerField(choices=[(0, 'Лекция'), (1, 'Мастер-класс'), (2, 'Хакатон')], verbose_name='Категории'),
        ),
    ]
