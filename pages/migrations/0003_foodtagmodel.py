# Generated by Django 3.2.3 on 2021-07-17 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20210717_0832'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodTagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'food tag',
                'verbose_name_plural': 'food tags',
            },
        ),
    ]
