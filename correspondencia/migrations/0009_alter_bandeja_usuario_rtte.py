# Generated by Django 5.0 on 2023-12-05 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('correspondencia', '0008_rename_nombre_destno_bandeja_nombre_destino_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bandeja',
            name='usuario_rtte',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
