# Generated by Django 3.2.3 on 2021-07-17 03:40

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20210716_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogTagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'blog tag',
                'verbose_name_plural': 'blog tags',
            },
        ),
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='name')),
                ('title_en', models.CharField(max_length=25, null=True, verbose_name='name')),
                ('title_uz', models.CharField(max_length=25, null=True, verbose_name='name')),
                ('title_ru', models.CharField(max_length=25, null=True, verbose_name='name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.RemoveField(
            model_name='blogmodel',
            name='description',
        ),
        migrations.RemoveField(
            model_name='blogmodel',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='blogmodel',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='blogmodel',
            name='description_uz',
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='long_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='', verbose_name='long descriptions'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='long_description_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='long descriptions'),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='long_description_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='long descriptions'),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='long_description_uz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='long descriptions'),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='short_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='', verbose_name='short descriptions'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='short_description_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='short descriptions'),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='short_description_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='short descriptions'),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='short_description_uz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='short descriptions'),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='post', to='post.categorymodel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='tags',
            field=models.ManyToManyField(related_name='post', to='post.BlogTagModel'),
        ),
    ]
