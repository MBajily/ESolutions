# Generated by Django 3.2 on 2021-06-15 13:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0069_clients_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 15, 16, 9, 16, 828750), null=True),
        ),
    ]
