# Generated by Django 5.1.4 on 2024-12-17 17:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='site_slogan',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]