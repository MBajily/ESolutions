# Generated by Django 3.2 on 2021-05-20 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0058_partners'),
    ]

    operations = [
        migrations.AddField(
            model_name='mail',
            name='is_trashed',
            field=models.CharField(default='0', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='mail',
            name='is_read',
            field=models.CharField(default='1', max_length=10, null=True),
        ),
    ]