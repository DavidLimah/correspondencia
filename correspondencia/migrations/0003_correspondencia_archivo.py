# Generated by Django 5.0 on 2024-01-04 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('correspondencia', '0002_remove_correspondencia_nombre_unidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='correspondencia',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
    ]