# Generated by Django 3.2 on 2021-05-02 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0047_alter_job_applied_cv_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client_cv',
            old_name='phone',
            new_name='phone1',
        ),
        migrations.AddField(
            model_name='client_cv',
            name='phone2',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
