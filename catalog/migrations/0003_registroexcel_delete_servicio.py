# Generated by Django 5.0.2 on 2024-02-26 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_datoscmpcchile_servicio_delete_asistencia_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroExcel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('area', models.CharField(max_length=100)),
                ('depdencia', models.CharField(max_length=100)),
                ('detalle', models.TextField()),
                ('frecuencia', models.CharField(max_length=100)),
                ('procedimiento', models.TextField()),
                ('parametro_control', models.CharField(max_length=100)),
                ('horario', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Servicio',
        ),
    ]
