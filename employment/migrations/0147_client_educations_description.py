# Generated by Django 4.0 on 2022-01-06 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0146_client_cv_cv_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='client_educations',
            name='description',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]