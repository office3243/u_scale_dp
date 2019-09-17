# Generated by Django 2.2.5 on 2019-09-17 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('materials', '0001_initial'),
        ('parties', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RateGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('extra_info', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MaterialRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('extra_info', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materials.Material')),
                ('parties', models.ManyToManyField(to='parties.Party')),
                ('rate_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rates.RateGroup')),
            ],
            options={
                'unique_together': {('material', 'rate_group')},
            },
        ),
    ]
