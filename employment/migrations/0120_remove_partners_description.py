# Generated by Django 4.0 on 2021-12-31 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0119_jobs_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partners',
            name='description',
        ),
    ]
