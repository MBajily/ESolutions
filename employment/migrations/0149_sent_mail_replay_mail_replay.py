# Generated by Django 4.0 on 2022-01-07 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('employment', '0148_alter_client_cv_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sent_Mail_Replay',
            fields=[
                ('replay_id', models.AutoField(primary_key=True, serialize=False)),
                ('sender', models.CharField(max_length=50, null=True)),
                ('message', models.CharField(max_length=2000, null=True)),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
                ('mail', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employment.sent_mail')),
            ],
        ),
        migrations.CreateModel(
            name='Mail_Replay',
            fields=[
                ('replay_id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=2000, null=True)),
                ('date_receive', models.DateTimeField(auto_now_add=True)),
                ('mail', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employment.mail')),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
