# Generated by Django 5.1.7 on 2025-03-26 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesapp', '0008_alter_movie_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='budget',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='overview',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='revenue',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='runtime',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
    ]
