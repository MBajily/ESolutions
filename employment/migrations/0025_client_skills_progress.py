# Generated by Django 3.1.6 on 2021-03-27 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0024_client_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='client_skills',
            name='progress',
            field=models.IntegerField(max_length=3, null=True),
        ),
    ]