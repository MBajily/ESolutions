# Generated by Django 4.0 on 2021-12-17 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0092_alter_partners_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partners',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='C:\\Users\\Mohammed Elgaily\\Django\\ES\\media'),
        ),
    ]
