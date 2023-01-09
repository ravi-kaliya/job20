# Generated by Django 4.1.5 on 2023-01-09 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_alter_uploads_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadsFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files')),
                ('description', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'UploadsFiles',
                'verbose_name_plural': 'UploadsFiless',
            },
        ),
    ]