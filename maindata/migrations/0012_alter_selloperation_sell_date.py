# Generated by Django 4.2.4 on 2024-01-17 20:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maindata', '0011_alter_client_options_selloperation_sellprocess_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selloperation',
            name='sell_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 17, 22, 23, 43, 18051), null=True, verbose_name=' تاريخ الخروج'),
        ),
    ]
