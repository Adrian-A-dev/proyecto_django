# Generated by Django 3.1.2 on 2020-11-05 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20201105_1256'),
    ]

    operations = [
        migrations.RenameField(
            model_name='insumo',
            old_name='presio',
            new_name='precio',
        ),
        migrations.RenameField(
            model_name='servicio',
            old_name='presio',
            new_name='precio',
        ),
        migrations.AlterField(
            model_name='insumo',
            name='descripcion',
            field=models.TextField(max_length=200),
        ),
    ]