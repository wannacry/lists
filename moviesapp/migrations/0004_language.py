# Generated by Django 5.1.7 on 2025-03-25 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesapp', '0003_alter_country_english_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('iso_639_1', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('english_name', models.CharField(max_length=100)),
                ('name', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
