# Generated by Django 2.2.5 on 2019-10-10 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0010_payment_created_on'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accounttransaction',
            old_name='unique_id',
            new_name='payment_code',
        ),
    ]
