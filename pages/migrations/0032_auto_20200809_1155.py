# Generated by Django 3.0.6 on 2020-08-09 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0031_inquiry_todo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todo',
            new_name='Task',
        ),
    ]