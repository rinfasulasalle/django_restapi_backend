# Generated by Django 4.2.7 on 2023-11-23 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_trabajador_sueldo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('usuario_id', models.CharField(max_length=20)),
                ('empleo_departamento', models.CharField(default=None, max_length=100, null=True)),
                ('empleo_cargo', models.CharField(default=None, max_length=100, null=True)),
                ('id_contrato_opcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dropdowncontratoopcion')),
                ('id_contrato_tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dropdowntipocontrato')),
                ('id_empleo_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dropdownareas')),
                ('id_empleo_proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dropdownproyecto')),
                ('id_empleo_proyecto_rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dropdownrolproyecto')),
                ('id_empleo_situacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dropdownempleosituacion')),
                ('id_empleo_tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dropdownempleotipo')),
                ('trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.trabajador')),
            ],
        ),
    ]
