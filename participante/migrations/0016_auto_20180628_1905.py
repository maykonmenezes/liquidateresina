# Generated by Django 2.0.6 on 2018-06-28 22:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participante', '0015_documentofiscal_qtdecupom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentofiscal',
            name='numeroDocumento',
            field=models.CharField(max_length=50, unique=True, verbose_name='Número do Documento'),
        ),
        migrations.AlterField(
            model_name='documentofiscal',
            name='qtdeCupom',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='documentofiscal',
            name='valorDocumento',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, validators=[django.core.validators.MinValueValidator(40, message='O valor do documento deve ser maior que 40 reais!')], verbose_name='Valor do Documento'),
        ),
        migrations.AlterField(
            model_name='documentofiscal',
            name='valorVirtual',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, editable=False, max_digits=20, verbose_name='Valor com Bonificações'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='RG',
            field=models.CharField(blank=True, max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='endereco',
            field=models.CharField(blank=True, max_length=150, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='enderecoComplemento',
            field=models.CharField(blank=True, max_length=100, verbose_name='Complemento'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='enderecoNumero',
            field=models.CharField(blank=True, max_length=200, verbose_name='Nº Endereço'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nome',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]