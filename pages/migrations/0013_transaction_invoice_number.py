# Generated by Django 3.0.6 on 2020-05-09 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_transaction_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='invoice_number',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
