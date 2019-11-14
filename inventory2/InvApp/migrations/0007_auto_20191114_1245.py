# Generated by Django 2.2.6 on 2019-11-14 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InvApp', '0006_auto_20191114_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armario',
            name='nombre',
            field=models.CharField(default='1', max_length=30),
        ),
        migrations.AlterField(
            model_name='laboratorio',
            name='ubicacion',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='objeto',
            name='condicion',
            field=models.IntegerField(choices=[(1, 'Nuevo'), (2, 'Usado'), (3, 'Arreglar'), (4, 'Roto')], default=1),
        ),
        migrations.AlterField(
            model_name='objeto',
            name='estado',
            field=models.IntegerField(choices=[(1, 'Prestado'), (2, 'Disponible'), (3, 'En mantenimiento')], default=1),
        ),
    ]