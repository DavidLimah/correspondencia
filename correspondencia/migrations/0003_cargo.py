# Generated by Django 5.0 on 2024-01-01 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('correspondencia', '0002_rename_sigla_unidad_tbconsejomunicipal_nombre_cargo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cargo', models.CharField(max_length=200)),
            ],
        ),
    ]
