# Generated by Django 4.0 on 2022-01-07 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0149_sent_mail_replay_mail_replay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail_replay',
            name='sender',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
