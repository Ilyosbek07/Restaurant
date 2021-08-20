# Generated by Django 3.2.3 on 2021-08-16 07:01

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0018_delete_chefmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChefsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='title')),
                ('title_uz', models.CharField(max_length=255, null=True, verbose_name='title')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='title')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='description')),
                ('description_en', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='description')),
                ('description_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='description')),
                ('description_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='description')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='image')),
                ('job', models.CharField(max_length=255, verbose_name='job')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'chef',
                'verbose_name_plural': 'chefs',
            },
        ),
    ]
