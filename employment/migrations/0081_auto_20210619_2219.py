# Generated by Django 3.2 on 2021-06-19 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0080_alter_client_cv_personal_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='full_name',
        ),
        migrations.AddField(
            model_name='clients',
            name='first_name',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='last_name',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='personal_id',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='second_name',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='third_name',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
