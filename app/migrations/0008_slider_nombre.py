# Generated by Django 3.1.2 on 2020-11-05 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='nombre',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
