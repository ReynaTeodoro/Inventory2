# Generated by Django 2.2.7 on 2019-12-02 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InvApp', '0012_auto_20191201_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='laboratorio',
            name='especialidad',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='InvApp.Especialidad'),
        ),
        migrations.AlterField(
            model_name='laboratorio',
            name='ubicacion',
            field=models.IntegerField(),
        ),
    ]