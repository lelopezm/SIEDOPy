# Generated by Django 4.2.6 on 2023-10-08 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_euler_nm_ciclos_remove_euler_nm_tiempo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='euler_nm',
            old_name='f',
            new_name='func',
        ),
    ]