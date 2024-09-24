# Generated by Django 5.1 on 2024-09-03 21:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agentes', '0012_remove_compensatorio_nombre_compensatorio_legajo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diaVacaciones', models.DateField()),
                ('vaca', models.IntegerField()),
                ('detalle', models.CharField(max_length=100)),
                ('motivo', models.IntegerField(choices=[(0, 'A tomar'), (1, 'Tomar')])),
                ('legajo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Agentes.agente')),
            ],
        ),
    ]