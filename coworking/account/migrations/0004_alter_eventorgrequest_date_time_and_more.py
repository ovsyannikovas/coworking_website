# Generated by Django 4.1.1 on 2022-12-17 20:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0003_remove_eventorgrequest_cat_eventorgrequest_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventorgrequest',
            name='date_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время проведения мероприятия'),
        ),
        migrations.AlterField(
            model_name='eventorgrequest',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Организатор'),
        ),
    ]