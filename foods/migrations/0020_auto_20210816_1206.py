# Generated by Django 3.2.3 on 2021-08-16 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0019_chefsmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chefsmodel',
            name='title',
        ),
        migrations.RemoveField(
            model_name='chefsmodel',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='chefsmodel',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='chefsmodel',
            name='title_uz',
        ),
    ]
