# Generated by Django 2.2.5 on 2019-09-26 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challans', '0004_challan_is_entry_done'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challan',
            name='payment_gateway_choice',
        ),
    ]
