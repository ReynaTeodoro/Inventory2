# Generated by Django 2.2.4 on 2019-12-01 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InvApp', '0012_auto_20191201_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratorio',
            name='ubicacion',
            field=models.IntegerField(),
        ),
    ]
