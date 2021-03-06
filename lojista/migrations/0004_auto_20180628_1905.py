# Generated by Django 2.0.6 on 2018-06-28 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lojista', '0003_auto_20180626_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lojista',
            name='IELojista',
            field=models.CharField(blank=True, max_length=14, null=True, unique=True, verbose_name='Inscrição Estadual'),
        ),
        migrations.AlterField(
            model_name='lojista',
            name='fantasiaLojista',
            field=models.CharField(help_text='Nome Fantasia', max_length=200, verbose_name='Nome Fantasia*'),
        ),
        migrations.AlterField(
            model_name='lojista',
            name='razaoLojista',
            field=models.CharField(blank=True, help_text='Razão Social', max_length=200, null=True, verbose_name='Razão Social*'),
        ),
    ]
