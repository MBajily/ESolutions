# Generated by Django 3.2 on 2021-04-25 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0035_auto_20210425_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='start_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
