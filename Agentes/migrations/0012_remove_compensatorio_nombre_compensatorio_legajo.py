# Generated by Django 4.2.1 on 2024-08-29 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Agentes', '0011_remove_compensatorio_legajo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compensatorio',
            name='nombre',
        ),
        migrations.AddField(
            model_name='compensatorio',
            name='legajo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Agentes.agente'),
        ),
    ]