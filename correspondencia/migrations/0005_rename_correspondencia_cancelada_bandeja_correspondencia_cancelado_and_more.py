# Generated by Django 5.0 on 2023-12-05 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('correspondencia', '0004_alter_bandeja_asunto_hoja_ruta_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bandeja',
            old_name='correspondencia_cancelada',
            new_name='correspondencia_cancelado',
        ),
        migrations.RenameField(
            model_name='bandeja',
            old_name='correspondencia_derivada',
            new_name='correspondencia_derivado',
        ),
        migrations.RemoveField(
            model_name='bandeja',
            name='correspondencia_devuelta',
        ),
    ]
