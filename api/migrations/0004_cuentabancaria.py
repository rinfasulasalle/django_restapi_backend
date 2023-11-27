# Generated by Django 4.2.7 on 2023-11-23 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_contrato'),
    ]

    operations = [
        migrations.CreateModel(
            name='CuentaBancaria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('usuario_id', models.CharField(max_length=20)),
                ('cuenta_bancaria_sueldo_codigo_cci', models.CharField(blank=True, max_length=255, null=True)),
                ('cuenta_bancaria_sueldo_codigo', models.CharField(blank=True, max_length=255, null=True)),
                ('cuenta_bancaria_sueldo_banco', models.CharField(blank=True, max_length=255, null=True)),
                ('cuenta_bancaria_cts_codigo_cci', models.CharField(blank=True, max_length=255, null=True)),
                ('cuenta_bancaria_cts_codigo', models.CharField(blank=True, max_length=255, null=True)),
                ('cuenta_bancaria_cts_banco', models.CharField(blank=True, max_length=255, null=True)),
                ('trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.trabajador')),
            ],
        ),
    ]
