# Generated by Django 2.2.4 on 2019-11-08 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InvApp', '0002_auto_20191031_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conjunto',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InvApp.Categoria'),
        ),
    ]
