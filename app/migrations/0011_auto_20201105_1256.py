# Generated by Django 3.1.2 on 2020-11-05 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_nosotros'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insumo',
            name='marca',
        ),
        migrations.AlterField(
            model_name='insumo',
            name='descripcion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='insumo',
            name='nombre',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='nosotros',
            name='nosotros',
            field=models.TextField(max_length=500),
        ),
        migrations.DeleteModel(
            name='Marca',
        ),
    ]
