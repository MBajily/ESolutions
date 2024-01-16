# Generated by Django 4.0 on 2022-01-01 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0140_alter_partners_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_cv',
            name='cv_file',
            field=models.FileField(upload_to='C:\\Users\\Mohammed Elgaily\\Django\\ES\\media/Clients/CVs/'),
        ),
        migrations.AlterField(
            model_name='client_cv',
            name='photo',
            field=models.ImageField(null=True, upload_to='C:\\Users\\Mohammed Elgaily\\Django\\ES\\media/Clients/Images/'),
        ),
        migrations.AlterField(
            model_name='client_cv_educations',
            name='pdf_file',
            field=models.FileField(max_length=2000, null=True, upload_to='C:\\Users\\Mohammed Elgaily\\Django\\ES\\media/Clients/Certificates/'),
        ),
        migrations.AlterField(
            model_name='job_applied',
            name='cv_file',
            field=models.FileField(blank=True, null=True, upload_to='C:\\Users\\Mohammed Elgaily\\Django\\ES\\media/Clients/CVs/'),
        ),
        migrations.AlterField(
            model_name='partners',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
