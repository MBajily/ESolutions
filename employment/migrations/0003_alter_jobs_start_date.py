# Generated by Django 4.2.1 on 2024-01-22 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0002_admin_permission_client_courses_client_cv_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]