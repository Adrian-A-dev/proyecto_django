# Generated by Django 3.1.2 on 2020-12-09 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_clientes_rut'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Clientes',
        ),
        migrations.AlterField(
            model_name='insumo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='insumo'),
        ),
    ]
