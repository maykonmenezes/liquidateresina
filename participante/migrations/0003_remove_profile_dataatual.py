# Generated by Django 2.0.6 on 2018-06-18 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participante', '0002_profile_dataatual'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='dataAtual',
        ),
    ]
