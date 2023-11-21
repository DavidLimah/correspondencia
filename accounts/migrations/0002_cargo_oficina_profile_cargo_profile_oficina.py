# Generated by Django 4.2 on 2023-11-20 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cargo', models.CharField(max_length=150, unique=True, verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Oficina',
                'verbose_name_plural': 'Oficina',
            },
        ),
        migrations.CreateModel(
            name='Oficina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_oficina', models.CharField(max_length=150, unique=True, verbose_name='Oficina')),
            ],
            options={
                'verbose_name': 'Oficina',
                'verbose_name_plural': 'Oficina',
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='cargo',
            field=models.ManyToManyField(related_name='cargo', to='accounts.cargo'),
        ),
        migrations.AddField(
            model_name='profile',
            name='oficina',
            field=models.ManyToManyField(related_name='oficina', to='accounts.oficina'),
        ),
    ]