# Generated by Django 4.0 on 2022-01-06 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('employment', '0147_client_educations_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_cv',
            name='client',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
