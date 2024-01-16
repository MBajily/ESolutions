# Generated by Django 3.2 on 2021-05-03 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employment', '0050_alter_mail_date_receive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_applied',
            name='job',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='employment.jobs'),
        ),
        migrations.AlterField(
            model_name='mail',
            name='receiver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mail',
            name='sender',
            field=models.CharField(default='Excelent Solutions', max_length=50, null=True),
        ),
    ]
