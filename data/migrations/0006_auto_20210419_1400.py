# Generated by Django 3.1.7 on 2021-04-19 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_datadb_localidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datadb',
            name='localidade',
            field=models.CharField(max_length=30),
        ),
    ]