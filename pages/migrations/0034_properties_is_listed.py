# Generated by Django 3.0.6 on 2020-08-18 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0033_task_is_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='is_listed',
            field=models.BooleanField(default=False),
        ),
    ]
