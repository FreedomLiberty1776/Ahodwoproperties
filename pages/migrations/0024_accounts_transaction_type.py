# Generated by Django 3.0.6 on 2020-05-14 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0023_accounts_business'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='transaction_type',
            field=models.CharField(max_length=20, null=True),
        ),
    ]