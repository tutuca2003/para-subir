# Generated by Django 4.2.1 on 2024-08-26 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Agentes', '0010_compensatorio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compensatorio',
            name='legajo',
        ),
    ]
