# Generated by Django 3.0.6 on 2020-05-15 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0026_auto_20200515_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='business',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='post_ref',
            field=models.IntegerField(null=True),
        ),
    ]