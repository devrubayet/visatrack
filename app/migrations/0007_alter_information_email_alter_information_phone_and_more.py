# Generated by Django 5.1.4 on 2024-12-17 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_information_about_us_information_office_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='site_slogan',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='sitename',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='sociallink',
            field=models.TextField(blank=True, null=True),
        ),
    ]
