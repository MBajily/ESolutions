# Generated by Django 3.2 on 2021-04-28 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0037_alter_jobs_start_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client_contact_information',
            name='client',
        ),
        migrations.DeleteModel(
            name='Clients_Login',
        ),
        migrations.DeleteModel(
            name='Employees',
        ),
        migrations.DeleteModel(
            name='Employees_Login',
        ),
        migrations.DeleteModel(
            name='Client_Contact_Information',
        ),
    ]