# Generated by Django 4.0 on 2022-01-30 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0159_remove_clients_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='client_cv',
            name='bio',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]