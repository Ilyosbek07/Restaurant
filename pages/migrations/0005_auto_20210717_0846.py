# Generated by Django 3.2.3 on 2021-07-17 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_remove_ordermodel_food'),
        ('pages', '0004_auto_20210717_0840'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FoodModel',
        ),
        migrations.DeleteModel(
            name='FoodTagModel',
        ),
        migrations.DeleteModel(
            name='FoodyModel',
        ),
    ]
