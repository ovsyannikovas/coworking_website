# Generated by Django 4.1.1 on 2022-12-20 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_eventorgrequest_date_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventorgrequest',
            name='user',
            field=models.IntegerField(null=True, verbose_name='Организатор'),
        ),
    ]