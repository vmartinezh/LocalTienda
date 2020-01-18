# Generated by Django 3.0.2 on 2020-01-15 15:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colores',
            fields=[
                ('id_color', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Marcas',
            fields=[
                ('id_marca', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tallas',
            fields=[
                ('id_talla', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Prenda',
            fields=[
                ('id_prenda', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=200)),
                ('precio', models.PositiveIntegerField()),
                ('cantidad', models.SmallIntegerField()),
                ('id_color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Colores')),
                ('id_marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Marcas')),
                ('id_talla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Tallas')),
            ],
        ),
    ]
