# Generated by Django 2.2.5 on 2019-10-02 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_auto_20190928_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallettransaction',
            name='is_full_amount',
        ),
        migrations.AddField(
            model_name='accounttransaction',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='payments/account_transactions/photos/'),
        ),
        migrations.AddField(
            model_name='cashtransaction',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='payments/account_transactions/photos/'),
        ),
        migrations.AddField(
            model_name='payment',
            name='payed_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='accounttransaction',
            name='bank_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bank_accounts.BankAccount'),
        ),
        migrations.AlterField(
            model_name='cashtransaction',
            name='status',
            field=models.CharField(choices=[('PN', 'Pending'), ('DN', 'Done')], default='DN', max_length=2),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_mode',
            field=models.CharField(choices=[('DP', 'Direct Payment'), ('AL', 'Account Less')], default='AL', max_length=2),
            preserve_default=False,
        ),
    ]