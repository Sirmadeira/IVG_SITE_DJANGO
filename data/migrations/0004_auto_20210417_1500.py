# Generated by Django 3.1.7 on 2021-04-17 18:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20210416_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datadb',
            name='ano',
            field=models.IntegerField(error_messages={'required': 'Favor inserir uma ano'}, validators=[django.core.validators.MinValueValidator(1960, 'Favor inserir acima 1960.'), django.core.validators.MaxValueValidator(2023, 'Favor inserir abaixo 2023.')]),
        ),
        migrations.AlterField(
            model_name='datadb',
            name='combustivel',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='datadb',
            name='cor',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='datadb',
            name='lucro',
            field=models.DecimalField(decimal_places=2, error_messages={'decimal_places': 'Favor so por 2 casas decimais.', 'max_digits': 'Favor inserir um lucro menor.', 'required': 'Favor inserir o lucro'}, max_digits=10, max_length=12),
        ),
        migrations.AlterField(
            model_name='datadb',
            name='marca',
            field=models.CharField(error_messages={'required': 'Favor inserir uma marca'}, max_length=30),
        ),
        migrations.AlterField(
            model_name='datadb',
            name='margem_de_lucro',
            field=models.DecimalField(decimal_places=3, max_digits=10, max_length=12),
        ),
        migrations.AlterField(
            model_name='datadb',
            name='modelo',
            field=models.CharField(error_messages={'required': 'Favor inserir um modelo'}, max_length=60),
        ),
        migrations.AlterField(
            model_name='datadb',
            name='preco',
            field=models.DecimalField(decimal_places=2, error_messages={'decimal_places': 'Favor so por 2 casas decimais.', 'max_digits': 'Favor inserir um lucro menor.', 'required': 'Favor inserir o lucro'}, max_digits=10, max_length=12),
        ),
        migrations.AlterField(
            model_name='datadb',
            name='quilometragem',
            field=models.DecimalField(decimal_places=2, error_messages={'decimal_places': 'Favor so por 2 casas decimais.', 'max_digits': 'Favor inserir uma kilometragem menor.', 'required': 'Favor inserir a quilometragem'}, max_digits=10, max_length=12),
        ),
    ]
