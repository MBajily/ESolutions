# Generated by Django 3.2 on 2021-04-15 12:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0031_job_applied'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_applied',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 4, 15, 15, 27, 6, 319414)),
        ),
    ]
