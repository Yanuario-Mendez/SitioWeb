# Generated by Django 4.2.7 on 2023-11-05 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0003_remove_cita_paciente_cita_nombre_cita_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='telefono',
            field=models.CharField(default='', max_length=20),
        ),
    ]