# Generated by Django 2.0.6 on 2018-06-26 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participante', '0012_auto_20180626_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentofiscal',
            name='key',
            field=models.BinaryField(max_length=100, null=True),
        ),
    ]
