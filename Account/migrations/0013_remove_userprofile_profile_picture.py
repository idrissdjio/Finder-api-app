# Generated by Django 3.2.2 on 2021-05-27 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0012_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_picture',
        ),
    ]
