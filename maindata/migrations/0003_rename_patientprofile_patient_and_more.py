# Generated by Django 4.2 on 2023-12-14 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maindata', '0002_cost_profile_file_profile_medicin_profile_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PatientProfile',
            new_name='Patient',
        ),
        migrations.RenameField(
            model_name='session',
            old_name='profile',
            new_name='patient',
        ),
        migrations.RemoveField(
            model_name='cost',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='file',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='medicin',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='paid',
            name='profile',
        ),
    ]
