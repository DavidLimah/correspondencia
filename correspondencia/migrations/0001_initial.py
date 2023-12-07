# Generated by Django 5.0 on 2023-12-07 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bandeja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, default='S/C', max_length=20, null=True)),
                ('usuario_rtte', models.CharField(blank=True, max_length=20, null=True)),
                ('nombre_rtte', models.CharField(blank=True, max_length=200, null=True)),
                ('oficina_rtte', models.CharField(blank=True, max_length=200, null=True)),
                ('cargo_rtte', models.CharField(blank=True, max_length=200, null=True)),
                ('numero_fojas', models.IntegerField(blank=True, null=True)),
                ('tipo_hoja_ruta', models.IntegerField(choices=[(0, 'Informe'), (1, 'Nota interna'), (2, 'Nota externa')])),
                ('usuario_destino', models.CharField(blank=True, max_length=200, null=True)),
                ('nombre_destino', models.CharField(blank=True, max_length=200, null=True)),
                ('oficina_destino', models.CharField(blank=True, max_length=200, null=True)),
                ('cargo_destino', models.CharField(blank=True, max_length=200, null=True)),
                ('derivado', models.BooleanField(blank=True, default=False, null=True)),
                ('recibido', models.BooleanField(blank=True, default=False, null=True)),
                ('devuelto', models.BooleanField(blank=True, default=False, null=True)),
                ('cancelado', models.BooleanField(blank=True, default=False, null=True)),
                ('archivado', models.BooleanField(blank=True, default=False, null=True)),
                ('pendiente', models.BooleanField(blank=True, default=False, null=True)),
                ('fecha_derivado', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha_recibido', models.DateTimeField(blank=True, null=True)),
                ('fecha_devuelto', models.DateTimeField(blank=True, null=True)),
                ('fecha_cancelado', models.DateTimeField(blank=True, null=True)),
                ('fecha_archivado', models.DateTimeField(blank=True, null=True)),
                ('asunto_hoja_ruta', models.CharField(blank=True, max_length=300, null=True)),
                ('asunto_devuelto', models.CharField(blank=True, max_length=200, null=True)),
                ('asunto_cancelado', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'bandeja',
                'verbose_name_plural': 'bandeja',
            },
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cargo', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'cargo',
                'verbose_name_plural': 'cargos',
            },
        ),
        migrations.CreateModel(
            name='Enviado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_remitente', models.CharField(blank=True, max_length=200, null=True)),
                ('of_remitente', models.CharField(blank=True, max_length=200, null=True)),
                ('car_remitente', models.CharField(blank=True, max_length=200, null=True)),
                ('user_destinatario', models.CharField(blank=True, max_length=200, null=True)),
                ('asunto_hr', models.CharField(blank=True, max_length=200, null=True)),
                ('num_fojas', models.IntegerField(blank=True, null=True)),
                ('estado', models.BooleanField(blank=True, default=True, null=True)),
            ],
            options={
                'verbose_name': 'enviado',
                'verbose_name_plural': 'enviados',
            },
        ),
        migrations.CreateModel(
            name='Oficina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_oficina', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'oficina',
                'verbose_name_plural': 'oficinas',
            },
        ),
    ]
