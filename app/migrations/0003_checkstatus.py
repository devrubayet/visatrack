# Generated by Django 5.1.4 on 2024-12-10 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_info_information'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_number', models.CharField(max_length=100, unique=True)),
                ('visa_name', models.CharField(max_length=100)),
                ('visa_status', models.CharField(max_length=100)),
                ('applicant_name', models.CharField(blank=True, max_length=100, null=True)),
                ('submission_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
