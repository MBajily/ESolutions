# Generated by Django 3.1.6 on 2021-02-26 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0016_auto_20210226_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='birth_date',
            field=models.DateField(default='01-01-2000'),
        ),
    ]