# Generated by Django 2.2.6 on 2019-10-12 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parties', '0002_remove_wallet_upper_limit'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='upper_limit',
            field=models.DecimalField(decimal_places=2, default=20000.0, max_digits=9),
        ),
    ]
