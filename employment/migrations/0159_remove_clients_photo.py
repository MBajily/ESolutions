# Generated by Django 4.0 on 2022-01-24 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0158_remove_client_courses_pdf_file_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='photo',
        ),
    ]