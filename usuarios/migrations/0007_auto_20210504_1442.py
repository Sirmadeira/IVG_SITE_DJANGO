# Generated by Django 3.1.7 on 2021-05-04 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_recomendacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recomendacao',
            name='texto',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='recomendacao',
            name='titulo',
            field=models.CharField(max_length=30),
        ),
    ]
