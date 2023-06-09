# Generated by Django 3.1.2 on 2020-12-10 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='contacto',
            name='tipo_contacto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.tipo_contacto'),
        ),
    ]
