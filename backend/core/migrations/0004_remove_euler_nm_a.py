# Generated by Django 4.2.6 on 2023-10-08 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_f_euler_nm_func'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='euler_nm',
            name='a',
        ),
    ]
