# Generated by Django 2.2.6 on 2019-11-14 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InvApp', '0005_auto_20191114_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='armario',
            name='nombre',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='laboratorio',
            name='ubicacion',
            field=models.CharField(max_length=30),
        ),
    ]
