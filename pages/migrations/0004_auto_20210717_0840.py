# Generated by Django 3.2.3 on 2021-07-17 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_foodtagmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodtagmodel',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='foodtagmodel',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='foodtagmodel',
            name='title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='name'),
        ),
    ]
