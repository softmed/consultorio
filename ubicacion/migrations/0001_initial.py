# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-16 10:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('maestras', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Areas',
            },
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Ciudades',
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Departamentos',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Paises',
            },
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ubicacion.Ciudad')),
            ],
            options={
                'verbose_name_plural': 'Sedes',
            },
        ),
        migrations.CreateModel(
            name='TipoUbicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Tipos de Ubicacion',
            },
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('estado', models.BooleanField()),
                ('horario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='maestras.Horario')),
                ('sede', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ubicacion.Sede')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ubicacion.TipoUbicacion')),
            ],
            options={
                'verbose_name_plural': 'Ubicaciones',
            },
        ),
        migrations.AddField(
            model_name='departamento',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ubicacion.Pais'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ubicacion.Departamento'),
        ),
    ]