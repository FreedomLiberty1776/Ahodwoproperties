# Generated by Django 3.0.6 on 2020-08-09 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0032_auto_20200809_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]