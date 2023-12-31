# Generated by Django 5.0 on 2023-12-05 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('correspondencia', '0002_enviado_alter_bandeja_options_alter_cargo_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enviado',
            name='asunto_hr',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='enviado',
            name='car_remitente',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='enviado',
            name='num_fojas',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='enviado',
            name='of_remitente',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='enviado',
            name='user_destinatario',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='enviado',
            name='user_remitente',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
