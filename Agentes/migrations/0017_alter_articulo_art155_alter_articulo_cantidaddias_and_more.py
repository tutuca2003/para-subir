# Generated by Django 5.1 on 2024-09-05 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agentes', '0016_alter_articulo_art155_alter_articulo_cantidaddias_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='art155',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='cantidadDias',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='cantidadHoras',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='com',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='parentesco',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
