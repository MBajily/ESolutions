# Generated by Django 3.2 on 2021-04-28 00:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employment', '0038_auto_20210428_0316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client_CV',
            fields=[
                ('cv_id', models.AutoField(primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=200, null=True)),
                ('photo', models.ImageField(null=True, upload_to='MEDIA_ROOT/Clients/Images/')),
                ('cv_file', models.FileField(upload_to='MEDIA_ROOT/Clients/CVs/')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employment.cities')),
                ('client_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('nationality', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employment.nationalities')),
                ('specialization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employment.specializations')),
            ],
        ),
    ]
