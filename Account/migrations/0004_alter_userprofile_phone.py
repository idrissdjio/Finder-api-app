# Generated by Django 3.2.2 on 2021-05-08 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0003_alter_userprofile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
