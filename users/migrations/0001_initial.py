# Generated by Django 3.2.3 on 2021-07-16 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=55, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=55, null=True, verbose_name='last name')),
                ('phone', models.IntegerField(blank=True, null=True, verbose_name='phone')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email')),
                ('company', models.CharField(blank=True, max_length=55, null=True, verbose_name='company')),
                ('country', models.CharField(blank=True, max_length=55, null=True, verbose_name='country')),
                ('address1', models.CharField(blank=True, max_length=55, null=True, verbose_name='address1')),
                ('address2', models.CharField(blank=True, max_length=55, null=True, verbose_name='address2')),
                ('city', models.CharField(blank=True, max_length=55, null=True, verbose_name='city')),
                ('state', models.CharField(blank=True, max_length=55, null=True, verbose_name='state')),
                ('postcode', models.CharField(blank=True, max_length=55, null=True, verbose_name='post code')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
            },
        ),
    ]