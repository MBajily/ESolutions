# Generated by Django 3.2 on 2021-06-15 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0070_alter_clients_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
