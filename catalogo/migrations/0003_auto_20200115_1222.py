# Generated by Django 3.0.2 on 2020-01-15 16:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_auto_20200115_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prenda',
            name='id_prenda',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='prenda',
            name='nombre',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
