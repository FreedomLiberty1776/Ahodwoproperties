# Generated by Django 3.0.6 on 2020-05-10 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0019_accounts_agent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='credit',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='debit',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]