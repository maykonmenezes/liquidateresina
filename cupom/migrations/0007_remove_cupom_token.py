# Generated by Django 2.0.6 on 2018-06-26 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cupom', '0006_auto_20180626_1311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cupom',
            name='token',
        ),
    ]
