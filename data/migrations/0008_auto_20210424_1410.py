# Generated by Django 3.1.7 on 2021-04-24 17:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_auto_20210424_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datadb',
            name='lucro',
            field=models.DecimalField(decimal_places=2, error_messages={'decimal_places': 'Favor so por 2 casas decimais.', 'max_digits': 'Favor inserir um lucro menor.', 'required': 'Favor inserir o lucro'}, max_digits=12, max_length=12, validators=[django.core.validators.MaxValueValidator(99999999, 'Favor inserir valor menor')]),
        ),
        migrations.AlterField(
            model_name='datadb',
            name='margem_de_lucro',
            field=models.DecimalField(decimal_places=3, max_digits=12, max_length=12),
        ),
        migrations.AlterField(
            model_name='datadb',
            name='preco',
            field=models.DecimalField(decimal_places=2, error_messages={'decimal_places': 'Favor so por 2 casas decimais.', 'max_digits': 'Favor inserir um lucro menor.', 'required': 'Favor inserir o lucro'}, max_digits=12, max_length=12, validators=[django.core.validators.MinValueValidator(1000.0, 'Favor inserir vendas acima de 1000 reais'), django.core.validators.MaxValueValidator(99999999, 'Favor inserir valor menor')]),
        ),
    ]
