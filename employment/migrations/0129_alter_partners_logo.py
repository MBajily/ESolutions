# Generated by Django 4.0 on 2022-01-01 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0128_alter_partners_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partners',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
