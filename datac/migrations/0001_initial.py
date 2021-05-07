# Generated by Django 3.1.7 on 2021-05-07 14:28

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DataDBC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(error_messages={'required': 'Favor inserir uma marca'}, max_length=30)),
                ('modelo', models.CharField(error_messages={'required': 'Favor inserir um modelo'}, max_length=60)),
                ('motor', models.CharField(error_messages={'required': 'Favor inserir um motor'}, max_length=60)),
                ('ano', models.IntegerField(error_messages={'required': 'Favor inserir uma ano'}, validators=[django.core.validators.MinValueValidator(1960, 'Favor inserir acima 1960.'), django.core.validators.MaxValueValidator(2023, 'Favor inserir abaixo 2023.')])),
                ('localidade', models.CharField(choices=[('P', 'Piracicaba'), ('L', 'Limeira')], max_length=1)),
                ('status', models.CharField(choices=[('E', 'Excelente'), ('B', 'Bom'), ('M', 'Mediano'), ('R', 'Ruim'), ('T', 'Terrível')], max_length=1)),
                ('cor', models.CharField(max_length=20)),
                ('combustivel', models.CharField(choices=[('G', 'Gasolina'), ('E', 'Etanol'), ('G', 'GNV'), ('D', 'Diesel'), ('F', 'Flex')], max_length=1)),
                ('quilometragem', models.DecimalField(decimal_places=2, max_digits=10, max_length=12, validators=[django.core.validators.MinValueValidator(0, 'Não existe quilometragem negativa'), django.core.validators.MaxValueValidator(99999999, 'Favor inserir valor menor')])),
                ('preco', models.DecimalField(decimal_places=2, max_digits=12, max_length=12, validators=[django.core.validators.MinValueValidator(1000.0, 'Favor inserir vendas acima de 1000 reais'), django.core.validators.MaxValueValidator(99999999, 'Favor inserir valor menor')])),
                ('data_postada', models.DateTimeField(default=django.utils.timezone.now)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
