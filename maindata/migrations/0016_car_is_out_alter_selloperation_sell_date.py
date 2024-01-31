# Generated by Django 4.2.4 on 2024-01-20 19:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maindata', '0015_alter_selloperation_sell_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='is_out',
            field=models.BooleanField(default=False, editable=False, verbose_name=' تم الخروج؟'),
        ),
        migrations.AlterField(
            model_name='selloperation',
            name='sell_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 20, 21, 0, 2, 684625), null=True, verbose_name=' تاريخ الخروج'),
        ),
    ]
