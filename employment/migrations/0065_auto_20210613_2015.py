# Generated by Django 3.2 on 2021-06-13 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0064_rename_sick_phone_interviews_has_health_condition'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone_interviews',
            name='position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employment.specializations'),
        ),
        migrations.AddField(
            model_name='phone_interviews',
            name='result',
            field=models.CharField(choices=[('Successed', 'Successed - ناجح'), ('Failed', 'Failed - راسب')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='phone_interviews',
            name='suited_job',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employment.jobs'),
        ),
        migrations.AlterField(
            model_name='phone_interviews',
            name='how_heared_about_job',
            field=models.CharField(choices=[('Friend', 'Friend - صديق'), ('ES Website', 'ES Website - موقع الحلول الممتازة'), ('Social Media', 'Social Media - منصات التواصل الإجتماعي')], max_length=200, null=True),
        ),
    ]