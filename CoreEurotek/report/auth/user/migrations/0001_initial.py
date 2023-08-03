# Generated by Django 4.2.3 on 2023-08-01 21:48

import django.core.validators
from django.db import migrations, models
import phonenumber_field.modelfields
import report


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('employee_id', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999)])),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=report.auth.user.models.image_path)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]