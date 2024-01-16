# Generated by Django 3.1.6 on 2021-03-27 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0023_auto_20210301_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client_Skills',
            fields=[
                ('skill_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, null=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employment.clients')),
            ],
        ),
    ]
