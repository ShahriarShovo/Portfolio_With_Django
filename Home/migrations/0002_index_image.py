# Generated by Django 4.0.3 on 2022-03-15 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]
