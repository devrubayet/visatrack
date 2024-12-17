# Generated by Django 5.1.4 on 2024-12-17 20:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_visaimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisaSilderImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='visa_images/')),
                ('visa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='app.visalist')),
            ],
        ),
        migrations.DeleteModel(
            name='VisaImage',
        ),
    ]
