# Generated by Django 3.2.2 on 2021-05-10 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SelectChoice', '0001_initial'),
        ('SearchApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postsearch',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SelectChoice.item_category'),
        ),
        migrations.AlterField(
            model_name='postsearch',
            name='city_lost',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SelectChoice.item_city'),
        ),
        migrations.DeleteModel(
            name='Lost_Item_Category',
        ),
        migrations.DeleteModel(
            name='Lost_Item_City',
        ),
    ]