# Generated by Django 4.0.5 on 2022-07-01 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantas',
            name='imagenPlanta',
            field=models.CharField(max_length=150, null=True, verbose_name='Imagen Planta'),
        ),
    ]