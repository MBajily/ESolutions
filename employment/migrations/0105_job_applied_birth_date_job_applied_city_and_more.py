# Generated by Django 4.0 on 2021-12-21 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('employment', '0104_remove_job_applied_birth_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_applied',
            name='birth_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='job_applied',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employment.cities'),
        ),
        migrations.AddField(
            model_name='job_applied',
            name='degree',
            field=models.CharField(choices=[('Intermediate School', 'Intermediate School - المرحلة الإبتدائية'), ('High School', 'High School - المرحلة الثانوية'), ('Deploma', 'Deploma - دبلوم'), ("Bachelor's Degree", "Bachelor's Degree - بكلاريوس"), ("Master's Degree", "Master's Degree - ماجستير"), ("PHD's Degree", "PHD's Degree - دكتوراه")], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='job_applied',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='job_applied',
            name='first_name',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='job_applied',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male - ذكر'), ('Female', 'Female - أنثى')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='job_applied',
            name='last_name',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='job_applied',
            name='nationality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employment.nationalities'),
        ),
        migrations.AddField(
            model_name='job_applied',
            name='personal_id',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='job_applied',
            name='phone_primary',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='job_applied',
            name='phone_secondary',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='job_applied',
            name='second_name',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='job_applied',
            name='specialization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employment.specializations'),
        ),
        migrations.AddField(
            model_name='job_applied',
            name='third_name',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='client_cv',
            name='cv_file',
            field=models.FileField(upload_to='C:\\Users\\Mohammed Elgaily\\Django\\ES\\static/media/Clients/CVs/'),
        ),
        migrations.AlterField(
            model_name='client_cv',
            name='photo',
            field=models.ImageField(null=True, upload_to='C:\\Users\\Mohammed Elgaily\\Django\\ES\\static/media/Clients/Images/'),
        ),
        migrations.AlterField(
            model_name='client_cv_educations',
            name='pdf_file',
            field=models.FileField(max_length=2000, null=True, upload_to='C:\\Users\\Mohammed Elgaily\\Django\\ES\\static/media/Clients/Certificates/'),
        ),
        migrations.AlterField(
            model_name='job_applied',
            name='client',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.user'),
        ),
        migrations.AlterField(
            model_name='job_applied',
            name='cv_file',
            field=models.FileField(blank=True, null=True, upload_to='C:\\Users\\Mohammed Elgaily\\Django\\ES\\static/media/Clients/CVs/'),
        ),
    ]
