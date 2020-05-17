# Generated by Django 3.0.6 on 2020-05-16 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0028_auto_20200516_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='rate_reference',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='accounts',
            name='usd_equi',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='accounts',
            name='usd_rate',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
