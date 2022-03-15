# Generated by Django 3.2 on 2022-03-14 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsite', '0012_auto_20220314_2059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='insta_url',
            new_name='github_url',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/profile/'),
        ),
    ]