# Generated by Django 4.2.3 on 2023-07-27 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0003_alter_pelicula_sinopsis_alter_serie_sinopsis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serie',
            name='f_fin',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='serie',
            name='f_inicio',
            field=models.DateField(),
        ),
    ]
