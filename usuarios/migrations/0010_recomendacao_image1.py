# Generated by Django 3.1.7 on 2021-05-04 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0009_auto_20210504_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='recomendacao',
            name='image1',
            field=models.ImageField(default='suamae.jpg', upload_to='graficos_recomendados'),
        ),
    ]