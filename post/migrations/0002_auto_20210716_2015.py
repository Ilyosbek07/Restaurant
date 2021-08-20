# Generated by Django 3.2.3 on 2021-07-16 15:15

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='first name')),
                ('last_name', models.CharField(max_length=255, verbose_name='last name')),
                ('message', models.TextField(null=True, verbose_name='message')),
                ('image', models.ImageField(null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comment',
            },
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='', verbose_name='detail motto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='description_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='detail motto'),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='description_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='detail motto'),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='description_uz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='detail motto'),
        ),
    ]