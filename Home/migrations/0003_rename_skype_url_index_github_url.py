# Generated by Django 4.0.3 on 2022-03-15 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_index_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='index',
            old_name='skype_url',
            new_name='github_url',
        ),
    ]