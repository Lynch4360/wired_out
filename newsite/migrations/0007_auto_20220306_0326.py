# Generated by Django 3.2 on 2022-03-06 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsite', '0006_auto_20220306_0323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='excerpt',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
    ]