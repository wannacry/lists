# Generated by Django 5.1.7 on 2025-03-20 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0002_alter_profile_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(upload_to='static/profile_img/'),
        ),
    ]
