# Generated by Django 3.2 on 2021-06-19 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0082_alter_clients_personal_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='personal_id',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]