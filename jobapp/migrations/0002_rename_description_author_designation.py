# Generated by Django 4.1.5 on 2023-01-09 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='description',
            new_name='designation',
        ),
    ]
